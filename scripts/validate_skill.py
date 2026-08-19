#!/usr/bin/env python3
"""Validate portable structure, state schema, links, and behavioral eval metadata."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_VERSION = "1.4.0"
SCHEMA_VERSION = "1"
STATE_FILES = {
    "course-map.md": "course-map",
    "learner-state.md": "learner-state",
    "session-log.md": "session-log",
}
REQUIRED_EVAL_CATEGORIES = {
    "startup",
    "safety",
    "mastery",
    "persistence",
    "lifecycle",
    "assessment",
}


def fail(message: str) -> None:
    raise ValueError(message)


def simple_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    try:
        block = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: unclosed frontmatter") from exc
    values: dict[str, str] = {}
    for line in block.splitlines():
        if not line or line.startswith(" ") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def validate_versions() -> None:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r'^\s+version:\s+"([^"]+)"\s*$', skill, re.MULTILINE)
    if not match or match.group(1) != SKILL_VERSION:
        fail(f"SKILL.md metadata version must be {SKILL_VERSION}")

    for filename, record_type in STATE_FILES.items():
        path = ROOT / "assets" / "course-state" / filename
        values = simple_frontmatter(path)
        expected = {
            "schema_version": SCHEMA_VERSION,
            "skill_version": SKILL_VERSION,
            "record_type": record_type,
            "revision": "0",
        }
        for key, value in expected.items():
            if values.get(key) != value:
                fail(f"{path.relative_to(ROOT)}: {key} must be {value!r}")
        for key in ("course_id", "created_at", "updated_at"):
            if key not in values:
                fail(f"{path.relative_to(ROOT)}: missing {key}")
    course_map = simple_frontmatter(ROOT / "assets" / "course-state" / "course-map.md")
    if course_map.get("tracking") != "active":
        fail("course-map.md: tracking must default to active")


def validate_relative_links() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        relative = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            file_target = target.split("#", 1)[0]
            resolved = (path.parent / file_target).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                fail(f"{relative}: link escapes skill root: {target}")
            if not resolved.exists():
                fail(f"{relative}: missing linked path: {target}")


def validate_evals() -> None:
    path = ROOT / "evals" / "cases.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("suite_version") != "1":
        fail("evals/cases.json: unsupported suite_version")
    if data.get("skill_version") != SKILL_VERSION:
        fail(f"evals/cases.json: skill_version must be {SKILL_VERSION}")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        fail("evals/cases.json: cases must be a non-empty list")

    ids: set[str] = set()
    categories: set[str] = set()
    required = {"id", "category", "prompt", "setup", "must", "must_not", "expected_writes"}
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            fail(f"eval case {index}: must be an object")
        missing = required - case.keys()
        if missing:
            fail(f"eval case {index}: missing {sorted(missing)}")
        case_id = case["id"]
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case_id):
            fail(f"eval case {index}: invalid id {case_id!r}")
        if case_id in ids:
            fail(f"evals/cases.json: duplicate id {case_id}")
        ids.add(case_id)
        categories.add(case["category"])
        for key in ("prompt", "setup"):
            if not isinstance(case[key], str) or not case[key].strip():
                fail(f"{case_id}: {key} must be non-empty")
        for key in ("must", "must_not", "expected_writes"):
            if not isinstance(case[key], list) or any(not isinstance(item, str) for item in case[key]):
                fail(f"{case_id}: {key} must be a list of strings")
        if not case["must"]:
            fail(f"{case_id}: must must contain observable acceptance criteria")

    missing_categories = REQUIRED_EVAL_CATEGORIES - categories
    if missing_categories:
        fail(f"evals/cases.json: missing categories {sorted(missing_categories)}")

    result_path = ROOT / "evals" / "result-template.json"
    result = json.loads(result_path.read_text(encoding="utf-8"))
    if result.get("suite_version") != data["suite_version"]:
        fail("evals/result-template.json: suite_version mismatch")
    if result.get("skill_version") != SKILL_VERSION:
        fail(f"evals/result-template.json: skill_version must be {SKILL_VERSION}")
    if not isinstance(result.get("results"), list) or not result["results"]:
        fail("evals/result-template.json: results must contain a sample entry")


def main() -> int:
    try:
        validate_versions()
        validate_relative_links()
        validate_evals()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1
    print("portable skill validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
