---
name: feature
description: Build an app feature end to end, from discovery through plan, design, build, review and retro, with a checkpoint after each phase.
disable-model-invocation: true
---

# Feature

Run one feature through six **phases**, in order. Each phase is its own skill and leaves one file in the **feature folder**, `.scratch/features/<slug>/`. Those files are the workflow's memory: any phase can resume from them in a fresh session.

| # | Phase    | Skill                                                 | Leaves         |
|---|----------|-------------------------------------------------------|----------------|
| 1 | Discover | [feature-discover](../feature-discover/SKILL.md)      | `discovery.md` |
| 2 | Plan     | [feature-plan](../feature-plan/SKILL.md)              | `plan.md`      |
| 3 | Design   | [feature-design](../feature-design/SKILL.md)          | `design.md`    |
| 4 | Build    | [feature-build](../feature-build/SKILL.md)            | `progress.md`  |
| 5 | Review   | [feature-review](../feature-review/SKILL.md)          | `review.md`    |
| 6 | Retro    | [feature-retro](../feature-retro/SKILL.md)            | `retro.md`     |

## Steps

1. **Find the feature folder.**
   - The argument names an existing folder under `.scratch/features/` → resume it.
   - Otherwise it describes a new feature → pick a short kebab-case slug, confirm it with the user, and create the folder.

   Make sure `.scratch/` is in the app repo's `.gitignore`; add it if missing.

2. **Find the current phase**: the first phase in the table whose file is missing or unfinished. Build is unfinished while `plan.md` has an unchecked slice; review is unfinished while `review.md` lists an open blocker.

3. **Run the phase**: read its skill file and follow it to its completion criterion.

4. **Checkpoint.** Show the user a summary of up to five lines: what the phase decided or produced, and anything it left open. Then ask: **continue**, **revise** this phase, or **stop** here. Move to the next phase only on *continue*. Review blockers send the work back to Build, then Review runs again.

5. Repeat steps 3–4 until `retro.md` exists.

## Skipping a phase

The user may skip a phase, for example Design for a one-line backend change. Write `Skipped: <reason>` as that phase's file, so the next resume finds the right phase.

## Context hygiene

Keep Discover, Plan and Design in one context window: each builds on the last one's thinking. At the Design → Build boundary, and between slices during Build when the window is large, suggest `/compact`. The feature folder holds everything the next phase needs.
