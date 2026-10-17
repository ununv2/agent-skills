---
name: feature-design
description: Feature phase 3. Design the UI, API contracts, modules and data for each slice in plan.md, and write design.md.
disable-model-invocation: true
---

# Feature: Design

Decide *how* each slice gets built, so implementation is mostly typing. There are two **tracks**. Run the ones the slices touch.

Works in the feature folder `.scratch/features/<slug>/` (see [feature](../feature/SKILL.md)). Reads `discovery.md` and `plan.md`.

## UI track

1. **Find the existing design language first**: tokens, theme, component library, and the exemplar screens from `discovery.md`. New UI extends it.
2. Invoke `ui-ux-pro-max` for layout, typography, colour, accessibility and stack-specific guidance. Use its design-system generator only when the app has no design language yet.
3. Invoke `apple-design` when a screen has gestures, sheets, drag, spring motion or translucent layers. Invoke `responsive-design` when layout must adapt across viewports.
4. For each screen, specify: layout per viewport; components (reused or new); every **state** (loading, empty, error, success, disabled); interactions and motion; accessibility (focus order, labels, contrast).
5. A UI question that is still unsettled on paper → use [prototype](../../design/prototype/SKILL.md) and record what it answered.

## Backend track

1. Invoke `codebase-design` for the vocabulary: aim for deep modules behind small interfaces, at clean seams.
2. For each endpoint, specify the **contract**: method and path, request, response, errors with status codes, and authorisation.
3. Specify data changes: schema, migrations, indexes, and backfill.
4. A module or API with several plausible shapes → invoke `design-an-interface` and record the chosen shape and why.
5. New domain terms or a hard-to-reverse decision → invoke `domain-model` to record it in the glossary or as an ADR.

## Write `design.md`

One section per slice, holding the screens and contracts it needs. File paths are fine here: this file is short-lived. End with **Decisions**, each with a one-line reason. Update `plan.md` if design changed a slice.

## Done when

Every slice in `plan.md` has its design covered, every screen lists all its states, and every endpoint lists its errors and authorisation.
