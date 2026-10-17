---
name: feature-build
description: Feature phase 4. Implement plan.md one slice at a time, test-first, logging progress in progress.md.
disable-model-invocation: true
---

# Feature: Build

Build the slices in `plan.md` one at a time, each fully **green** before the next starts.

Works in the feature folder `.scratch/features/<slug>/` (see [feature](../feature/SKILL.md)). Reads `discovery.md`, `plan.md`, `design.md` and `progress.md`.

## Before the first slice

Ask the user once: work on a feature branch? Commit after each slice? Record the answers at the top of `progress.md`.

## Per slice

1. **Pick** the first unchecked slice whose dependencies are checked.
2. **Build it**, copying patterns from the exemplar in `discovery.md` and following `design.md`:
   - Behaviour (API, domain logic, data): invoke `tdd`, one red-green-refactor cycle per acceptance criterion.
   - UI: build the screen and all its states from `design.md`, with component or integration tests where the project has them.
   - Servers needed: invoke `server-operations`.
3. **Stuck** on a failure → invoke `diagnosing-bugs`, or `frontend-runtime-debugging` for browser-side symptoms.
4. **Check**: run the project's lint, typecheck and tests from `discovery.md`. Run the slice once yourself and watch each acceptance criterion pass.
5. **Record**: tick the slice in `plan.md`. Append to `progress.md`:

   ```markdown
   ## S<n> <name> — done
   - Changed: <files/modules>
   - Deviations from design: <what and why, or "none">
   - Follow-ups: <anything noticed but out of scope>
   ```

   Commit if the user chose to.

## Done when

Every slice in `plan.md` is checked, and the full lint, typecheck and test run is green on the final state.
