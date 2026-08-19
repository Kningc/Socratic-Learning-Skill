# Agent compatibility and installation

The skill body is host-neutral. Install this entire repository as a directory named `socratic-learning` so relative links from `SKILL.md` continue to resolve.

## Native Agent Skills hosts

| Host | Personal or global skills root | Project or workspace skills root | Typical explicit invocation |
| --- | --- | --- | --- |
| OpenAI Codex | `${CODEX_HOME}/skills/` or `~/.codex/skills/` | Environment-dependent | `$socratic-learning` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` | `/socratic-learning` |
| Cursor | `~/.agents/skills/` or `~/.cursor/skills/` | `.agents/skills/` or `.cursor/skills/` | `/socratic-learning` |
| GitHub Copilot | `~/.agents/skills/` or `~/.copilot/skills/` | `.agents/skills/` or `.github/skills/` | `/socratic-learning` where supported |
| Gemini CLI | `~/.agents/skills/` or `~/.gemini/skills/` | `.agents/skills/` or `.gemini/skills/` | Ask Gemini to use `socratic-learning` |
| Windsurf Cascade | `~/.agents/skills/` or `~/.codeium/windsurf/skills/` | `.agents/skills/` or `.windsurf/skills/` | `@socratic-learning` |
| Cline | `~/.cline/skills/` | `.cline/skills/` | Ask Cline to use `socratic-learning` |
| OpenCode | `~/.agents/skills/` or `~/.config/opencode/skills/` | `.agents/skills/` or `.opencode/skills/` | `/socratic-learning` where supported |

Example personal installation for a host with its own directory:

```bash
git clone https://github.com/Kningc/Socratic-Learning-Skill.git ~/.claude/skills/socratic-learning
```

For a project-scoped installation, copy or add the repository under the corresponding project skills root. Do not copy only `SKILL.md`; the `references/` directory contains material-specific guidance loaded on demand.

## Shared `.agents/skills` location

The shared `.agents/skills/` convention reduces duplicate installations. At the time this guide was written, Cursor, GitHub Copilot, Gemini CLI, Windsurf, and OpenCode document support for it. Hosts may add support over time, so prefer their current documentation when choosing a path.

## Hosts without native Skill discovery

Any agent that can read files or accept attached context can still use the package:

1. Give the agent access to this repository.
2. Say: `Read SKILL.md and follow it to help me learn the supplied material.`
3. Keep the repository structure intact so the agent can open the referenced playbook when needed.

For an agent that accepts a persistent instruction file, use a short loader rather than duplicating the full Skill:

```markdown
When the user wants guided learning from supplied material, read
path/to/socratic-learning/SKILL.md and follow it. Resolve linked files relative
to that Skill directory.
```

This fallback preserves one source of truth and avoids maintaining divergent platform-specific prompts.

## Official host documentation

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Cursor Agent Skills](https://cursor.com/docs/skills)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/)
- [Windsurf Cascade Skills](https://docs.windsurf.com/windsurf/cascade/skills)
- [Cline Skills](https://docs.cline.bot/customization/skills)
- [OpenCode Agent Skills](https://opencode.ai/docs/skills)
