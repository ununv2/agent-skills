---
name: feature-retro
description: Feature phase 6. Look back on how the feature went, run /retro on the environment, and write retro.md.
disable-model-invocation: true
---

# Feature: Retro

Turn what went wrong, or slowly, during this feature into **lessons**, then into changes that make the next feature go better. A lesson names a specific moment and gets a fix. "Testing could be better" is not a lesson.

Works in the feature folder `.scratch/features/<slug>/` (see [feature](../feature/SKILL.md)). Reads every file in it, plus this session's history as primary source.

## Steps

1. **Look at the feature.** Compare what was planned with what happened:
   - **Discovery misses**: facts found during Build or Review that Discover should have found.
   - **Plan drift**: slices that were added, split or merged, and acceptance criteria that changed.
   - **Design drift**: the **Deviations** entries in `progress.md`, and why each happened.
   - **Review catches**: each blocker and should-fix in `review.md`, and which earlier phase could have prevented it.
   - **Friction**: where the session lost time, such as retries, wrong files, waiting on servers, or unclear instructions.

2. **Look at the environment.** Follow [retro](../../review/retro/SKILL.md) against this session. Its candidates cover navigation, automated checks, coding standards, steering files, tooling and access to information.

3. **Look at the workflow.** For each lesson from step 1 that traces back to a phase skill (`feature-*`) or a skill it invokes, propose an edit to that skill. Follow `writing-for-agents`.

4. **Write `retro.md`**:

   ```markdown
   # Retro: <feature>

   ## What happened
   <3–5 lines: planned vs actual, biggest surprise>

   ## Lessons
   <numbered: moment → cause → proposed change → where it goes (app repo / skill / CLAUDE.md / check)>
   ```

   Order lessons by how much time or risk they would have saved.

5. **Apply** only the changes the user approves. Tick each one in `retro.md` as it lands.

## Done when

Every review blocker, design deviation and point of friction has either a lesson or a stated reason it needs none, and every approved change is applied.
