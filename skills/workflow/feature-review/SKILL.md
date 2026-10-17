---
name: feature-review
description: Feature phase 5. Verify the built feature against plan.md and design.md with fresh evidence, review the diff, and write review.md.
disable-model-invocation: true
---

# Feature: Review

Treat the feature as **guilty until proven innocent**. Each claim in `review.md` rests on evidence gathered in this phase.

Works in the feature folder `.scratch/features/<slug>/` (see [feature](../feature/SKILL.md)). Reads `plan.md`, `design.md` and `progress.md`. The diff is the feature branch against its base. Without a branch, it is the commits and changes listed in `progress.md`.

## Steps

1. **Verify.** Invoke `verification-before-completion`. Its criteria source is every acceptance criterion in `plan.md` and every success criterion in `discovery.md`. Rate each one matches / deviates / not-addressed, with a confidence of HIGH / MEDIUM / LOW.

2. **Check the UI.** For each screen in `design.md`, invoke `visual-verification` in spec-conformance mode, checking its viewports and every state.

3. **Review the diff with fresh eyes.** Dispatch a subagent with the diff, `design.md`, and the project's `CLAUDE.md` / `CODING_STANDARDS.md`. It reports findings on:
   - **Spec**: the code does what `design.md` says, and deviations are logged in `progress.md`.
   - **Standards**: it matches the surrounding code and the project's written rules.
   - **Security**: new endpoints check authorisation, input is validated, and no secrets appear in code or logs.
   - **Simplicity**: dead code, duplication, needless abstraction.

4. **Guard it.** Invoke `derive-e2e-coverage` on the success criteria. List the resulting scenario specs in `review.md`. Offer to build them now as a final slice.

5. **Write `review.md`.** Put the criteria table from step 1 first. Then list every finding, tagged **blocker** (wrong behaviour, failed check, security hole), **should-fix** or **nit**, each with a file and line.

## Done when

Every criterion has a rating backed by a command or observation, and every finding is tagged. Open blockers send the work back to Build. When those are fixed, rerun this phase.
