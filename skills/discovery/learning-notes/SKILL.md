---
name: learning-notes
description: Turn a YouTube video, article, blog post or docs page into a study note in the user's Obsidian vault, written to teach a final-year computer engineering intern how the topic works in real production (the why, the how, the end-to-end flow, industry conventions, concrete examples). Use whenever the user pastes a youtube.com / youtu.be link or a web URL and wants it summarized, turned into notes, explained, "learned", or saved, or says things like "note this", "summarize this video", "I don't want to watch the whole thing", "what does this article teach", even if they don't mention notes or Obsidian. Also use for several links at once.
---

# Learning notes

Turn long videos and articles into notes the user can actually learn from, so they don't have to sit through a 40-minute video or a 5,000-word post.

## Who the notes are for

The user is a software engineering intern in their 4th year of computer engineering. They know the theory from class (data structures, networking, OS, databases, the SDLC) but have little hands-on experience with how real teams build and run software. What they want from each source:

- **How it works in production.** What does this look like at a real company? Which tools, conventions and standards do teams use? What do they do on an ordinary Tuesday?
- **Why before how.** What problem does this solve? What breaks without it? Why was it designed this way and not some other obvious way? Without the why, the how doesn't stick.
- **The end-to-end flow.** How a request, deploy, or piece of data moves through the whole system, step by step, from start to finish. Isolated facts don't build understanding; the story connecting them does.
- **Concrete examples for hard ideas.** A config file, a command, a sequence of requests, a small analogy, numbers. Show the idea in a form they can picture.

So don't just compress the source. Teach it. Keep everything important from the source, explain the parts a theory-only student would trip on, and fill in the production context the source assumes the viewer already knows.

## Workflow

### 1. Get the full source text

Read the whole source. A note built from a partial transcript or a summary of a summary misses the parts that matter.

- **YouTube** (`youtube.com`, `youtu.be`, shorts): run `python3 -I <skill-dir>/scripts/fetch_youtube.py "<url>" > <scratch>/source.txt` and read that file. It contains the title, channel, date, duration, chapters, description and a timestamped transcript in the video's own language. If it reports no transcript, tell the user and ask them to paste one. Don't write a note from the title and description alone.
- **Web pages**: run `python3 -I <skill-dir>/scripts/fetch_article.py "<url>" > <scratch>/source.txt` and read that file. It contains the full readable text, including code blocks. If it exits with code 2 (very little text: JS-rendered, paywalled or blocked), fall back to WebFetch, asking it for the complete article text verbatim. If that also fails, tell the user.
- **Multi-page docs**: if the link is one page of a larger guide and that page only makes sense with its neighbours, fetch the linked sub-pages it clearly depends on (keep it to a handful), and mention which pages you included.

Transcripts are long. Read the whole file in parts (e.g. `sed -n 1,80p`, `81,160p`, ...) rather than one huge read that gets truncated; a Thai transcript line can be very long because Thai has no spaces between words.

### 2. Understand before writing

Before you draft, work out:
- The single core idea, in one sentence.
- The problem it solves, and what people did before it.
- The flow: the sequence of steps from start to finish.
- What the source simplifies, skips or assumes, that a student would need to know to apply it at work.
- Anything outdated or debatable. Check against what you know of current practice, and use WebSearch if a version, tool or claim looks stale.

### 3. Write the note

Use the structure below. It is a default, not a cage: rename, merge or drop sections to fit the source (a talk about careers doesn't need a config example; a tool tutorial doesn't need an analogy). What must always survive is the TL;DR, the why, the how, the flow, the production reality, and examples where an idea is hard.

```markdown
---
title: "<original title of the source>"
source: <url>
channel: <channel>          # videos; for articles use `author:` and/or `site:`
published: YYYY-MM-DD       # if known
duration: 48m               # videos only
tags: [lowercase, hyphenated, flat-tags]
type: video-note            # or article-note
related: ["[[Existing Note]]"]
---

# <Topic>: <what it teaches>

## TL;DR
3-5 bullets someone could read in 30 seconds and walk away with the gist:
the problem, the answer the source gives, the key steps or rules, and the one
thing to remember or do at work. Concrete, no teasers ("the video explains...").

## 0. Read this first
- **What is it?** 2-3 plain sentences.
- **Core idea in one sentence** (as a > quote).
- **Why it matters at work**: the problem it solves, what goes wrong without it.
- Analogy, only if it actually clarifies something.
- **Glossary** table of terms the note uses that a student might not know yet.

## 1..N. The content, one section per concept or stage
For each concept, cover what it is, why it exists, how it works (with an
example: code, command, config, request sequence, numbers), and, where it adds
something, **In production** (what real teams do or use) and **Common mistake**.
End a dense section with a > 🔑 Takeaway line.

## End-to-end flow
A numbered story of the whole thing happening once, start to finish. A
mermaid diagram (Obsidian renders mermaid code blocks) helps when there are
branches or several components.

## In the real world
Conventions, standards and tools teams actually use; what the source
simplified; what's outdated or debated. Label anything that isn't from the
source (see "Source vs added context" below).

## Recap table

## Self-test
5-10 questions that test understanding, not recall. Scenario questions
("users get logged out at random behind a load balancer: what's the cause?")
beat definition questions.

## Where to go next
Links to related notes already in the vault, plus 1-3 concrete next things to
learn or try.

Timestamps (videos): key moments as `mm:ss Topic`, separated by ·
```

#### Writing guidance

- **Explain the why in the body**, not only in section 0. When a step looks arbitrary ("set `--max-surge 25%`"), say what it protects against.
- **Examples should be realistic.** Use plausible names (`orders-api`, `payments-db`), real tool syntax, and realistic numbers (latencies, sizes, counts). If you reconstruct code the source only described, say so in an italic line under it and point out anything version-sensitive.
- **Source vs added context.** The user needs to know what came from the source and what you added. Write the source's content plainly; mark your own additions (production context, corrections, modern practice) with a leading *(added)* or put them in clearly labelled places such as "In production" and "In the real world". If you think the source is wrong or outdated, say so and say why. Don't silently correct it.
- **Plain language, precise terms.** Define jargon on first use (or in the glossary), then use the real term consistently: the user needs the industry vocabulary.
- **Length follows content density, not duration.** A fluffy 30-minute video can become 40 lines; a dense 15-minute walkthrough may need 200. Drop filler, sponsor reads, intros and repetition. Never drop a step of a process.
- **Language: match the source.** An English source gets an English note. A Thai source gets a Thai note, with technical terms kept in English (e.g. "load balancer", "idempotent") because that's how they appear in docs and at work.
- Use **bold** for key terms and tables for comparisons. Use headings so the note can be skimmed later.

### 4. Save into the Obsidian vault

Vault: `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian Vault/`

- Folder: `002 - Knowledge/` (the user's existing home for video and article notes). If the user names a different folder, use that.
- File name: `<Topic> - <Short subtitle> (<Creator>).md`, e.g. `CI-CD with GitHub Actions - Beginner Guide (Nova Designs).md`. For articles the creator is the author, not the site (put both in frontmatter as `author:` and `site:`). Leave out `(<Creator>)` for official docs or standards (e.g. `Twelve-Factor App - Deployment Principles.md`). Strip characters that are illegal in file names (`/ \ : * ? " < > |`).
- If a note for the same source already exists, show the user and ask before overwriting.
- Before writing, list the `.md` files in the vault and link related ones with `[[Exact Note Name]]` in `related:` and "Where to go next". Only link notes that exist; Obsidian doesn't warn about broken links, so they silently rot. Don't edit the user's existing notes on your own. If one is closely related, offer in your reply to add a back-link to its "Where to go next".
- `Twelve-Factor App - Deployment Principles.md` in the same folder is a good example of the depth and tone to aim for, if you want a reference.

### 5. Reply in chat

Keep it short: a link that opens the note in Obsidian, `[<note name>](obsidian://open?vault=Obsidian%20Vault&file=002%20-%20Knowledge%2F<URL-encoded file name without .md>)`, the core idea in one or two sentences, and anything the user should know, such as an auto-generated transcript with garbled terms, sub-pages you pulled in, or a claim in the source you think is wrong. Don't paste the whole note into the chat.

## Several links at once

Write one note per source. If they cover the same topic, cross-link them and add a short "Comparison with ..." section to each saying how they differ or overlap. If the user explicitly wants a single combined note, write one note, list every source in `source:` (as a YAML list), and say which source each part comes from.
