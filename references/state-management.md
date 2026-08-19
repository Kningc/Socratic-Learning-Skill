# Persistent state management

Read this reference before creating, changing, migrating, exporting, pausing, or deleting long-form course state.

## State boundary

Persistent state is optional and learner-owned. Use the approved state directory, normally `.socratic-learning/` in the study workspace. Never write learner records into the installed Skill directory or sync them externally unless the learner explicitly requests that destination.

Keep state minimal. Record learning goals, source anchors, observable evidence, active misconceptions, review dates, completed activities, and next actions. Do not store full conversations, unnecessary source excerpts, inferred emotions, health information, credentials, unrelated personal details, or fictional scores.

## Schema 1

Every canonical state file begins with YAML frontmatter containing:

- `schema_version`: state schema, currently `"1"`;
- `skill_version`: Skill version that last wrote the file;
- `record_type`: `course-map`, `learner-state`, or `session-log`;
- `course_id`: the same stable, non-sensitive identifier across the course;
- `revision`: non-negative integer incremented on each successful write;
- `created_at` and `updated_at`: ISO 8601 timestamps with timezone when available.

The course map also contains `tracking: active` or `tracking: paused`. Pausing stops state writes and scheduling changes; it does not delete existing state.

Treat unknown fields as preserved extensions. Do not discard them merely because the current template does not define them.

## Safe writes and concurrent sessions

At session start, retain the revisions that were read. Immediately before a write, reread the target file:

- If its revision is unchanged, apply the update, increment the revision once, and update `skill_version` and `updated_at`.
- If its revision changed, do not overwrite it with the stale copy. Reconcile append-only facts when unambiguous; otherwise show the conflict and ask which state should prevail.
- If `course_id` or `record_type` differs, stop. The file belongs to another course or role.

When the host supports safe filesystem operations, write a complete validated sibling temporary file and replace the target atomically. Never leave a half-written canonical file. Preserve user additions and unrelated fields.

Session logs are append-oriented. If two sessions add entries, keep both and order them explicitly; do not rewrite history to make it appear sequential. When archiving, retain an index and the latest canonical state.

## Migration

Before writing, compare each file's schema with the supported schema:

- Same version: update normally.
- Older version: explain the migration, copy the current state to a timestamped backup, migrate only known fields, validate the result, and preserve the backup.
- Newer or unknown version: remain read-only and ask the learner to use a compatible Skill or approve a documented migration. Never guess and overwrite.

Migration must not silently change mastery judgments. Record structural transformations separately from new learning evidence.

## Data lifecycle

Support these learner-controlled operations:

- **Inspect:** summarize which files exist, what categories they contain, and where they are stored.
- **Pause:** set tracking to `paused`; continue teaching without writing until resumed.
- **Resume:** verify schema and revisions, then set tracking to `active` if the learner requests it.
- **Export:** copy the resolved state files to the learner's chosen local destination in a readable form; do not upload without separate authorization.
- **Reset a course:** preserve or archive the old state unless the learner explicitly requests deletion, then initialize a new course ID.
- **Delete:** resolve and display the exact course-state target. If the deletion request is explicit and unambiguous, follow the host's normal destructive-action policy and prefer recoverable trash. Never broaden deletion beyond that course directory.

After export, reset, or deletion, report what changed, what remains, and whether recovery is possible.
