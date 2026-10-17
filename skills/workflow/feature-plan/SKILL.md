---
name: feature-plan
description: Feature phase 2. Turn discovery.md into a spec and an ordered list of vertical slices in plan.md.
disable-model-invocation: true
---

# Feature: Plan

Turn what discovery found into a spec, and cut it into **tracer-bullet slices**: thin, vertical, end-to-end. Each slice runs from UI through API to data and can be demoed alone.

Works in the feature folder `.scratch/features/<slug>/` (see [feature](../feature/SKILL.md)). Reads `discovery.md`.

## Steps

1. **Write the spec.** Use the spec template in [to-spec](../../planning/to-spec/SKILL.md): problem, solution, user stories, implementation decisions, testing decisions, out of scope. Write it into `plan.md` instead of publishing it. Synthesise from `discovery.md`; interview only where it left a gap.

2. **Agree on test seams.** Propose the highest seams to test at, preferring existing ones (an HTTP route, a page, a public module API). Confirm them with the user.

3. **Slice it.** Append a `## Slices` section, ordered so each slice's dependencies come first:

   ```markdown
   - [ ] **S1 <name>** — <what a user can do after it>
     - Layers: UI / API / data
     - Depends on: —
     - Acceptance:
       - Given … when … then …
   ```

   The first slice is the thinnest path that proves the stack end to end. Use `user-story` for Gherkin acceptance criteria when a criterion is hard to phrase.

## Done when

Every success criterion in `discovery.md` maps to at least one slice's acceptance criteria. Every slice can be verified on its own, and the user agrees on the seams.
