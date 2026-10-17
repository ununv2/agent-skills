---
name: feature-discover
description: Feature phase 1. Gather what a feature needs from the codebase, docs and the user, and write discovery.md.
disable-model-invocation: true
---

# Feature: Discover

Learn enough about the feature, the codebase it lands in, and the outside docs it depends on that planning needs no guesswork. Facts are your job. Decisions belong to the user.

Works in the feature folder `.scratch/features/<slug>/` (see [feature](../feature/SKILL.md)). Run standalone, ask for the slug first.

## Steps

1. **Frame it.** Restate the feature as one sentence: who it is for, and what they can do afterwards that they can't now. Ask the user for any source material: tickets, designs, docs links, examples from other apps.

2. **Map the codebase.** Read `CLAUDE.md`/`AGENTS.md`, `CONTEXT.md` and `docs/adr/` if present. Then dispatch `Explore` subagents, one per area the feature touches (UI, API, data, auth, jobs), each returning:
   - entry points and files the feature will touch;
   - an **exemplar**: the closest existing feature to copy patterns from;
   - data models, API routes and shared components involved;
   - how that area is tested, and the commands to lint, typecheck, test and run it.

3. **Read the outside docs.** For each library, API or platform question the codebase can't answer, invoke the `research` skill and save its findings file into the feature folder. Send independent questions in parallel.

4. **Settle scope with the user.** Invoke `grill-with-docs` to interview the user on scope, users, edge cases and constraints, using what steps 2–3 found. Stop when every remaining question is either answered or one the user explicitly defers.

5. **Write `discovery.md`**:

   ```markdown
   # <Feature>
   <one-sentence goal>

   ## Success criteria
   <numbered, each phrased as something a user can observe>

   ## Codebase
   <touch points, exemplar, models/APIs/components, test approach, check commands>

   ## External docs
   <findings with links to the research files>

   ## Decisions
   <what the user decided in step 4>

   ## Constraints and risks

   ## Out of scope

   ## Deferred questions
   <question — who answers it — what it blocks>
   ```

## Done when

Every success criterion is observable by a user, every touch point names real files, and every open question is either answered in **Decisions** or listed under **Deferred questions**.
