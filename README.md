# agent-skills

My agent skills, grouped by the stage of work they help with.

```
skills/
├── discovery/       # understand the problem: research, grilling, questionnaires
├── planning/        # turn understanding into specs, stories, maps
├── design/          # shape interfaces, modules, UI systems
├── implementation/  # build, debug, hand off
└── meta/            # skills about skills
```

Each skill is a folder with a `SKILL.md` (frontmatter `name` + `description`) and optional supporting files.

## Use

**Symlink (day-to-day, edits apply instantly):**

```sh
./scripts/link.sh                                     # into ~/.claude/skills
./scripts/link.sh ~/.claude/skills ~/.agents/skills   # several agents at once
```

Re-run after adding or removing a skill. Skill folder names must be unique across categories.

**Plugin marketplace (other machines / sharing):**

```
/plugin marketplace add <github-user>/agent-skills
/plugin install implementation@unun-skills
```

Each category is its own plugin. Add new skills to its list in `.claude-plugin/marketplace.json`.

## Adding a skill

1. Create `skills/<category>/<name>/SKILL.md`.
2. Add it to `.claude-plugin/marketplace.json`.
3. Run `./scripts/link.sh`.

## Sources

- Copied from my claude.ai synced skills (several originally from [mattpocock/skills](https://github.com/mattpocock/skills)).
- `codebase-design`, `design-an-interface`, `domain-model`, `improve-codebase-architecture`, `grill-with-docs`, `research`, `research-recommend`, `session-bootstrap`, `zoom-out`, `architect-review`, `diagnosing-bugs`, `frontend-runtime-debugging`, `resolving-merge-conflicts`, `server-operations`, `tdd`, `skill-creator`: from [zentetsukenz/agent](https://github.com/zentetsukenz/agent/tree/main/SKILLS) @ `4d6d5b2`.
