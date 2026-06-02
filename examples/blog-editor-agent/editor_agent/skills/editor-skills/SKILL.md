---
name: editor-skills
description: Suggest  and improve blog posts, newsletters, or articles when the user asks to refine writing, improve clarity, strengthen flow, or make content more impactful while preserving the original voice.
license: Apache-2.0
metadata:
  author: Ayushi Sahu
  version: "2.0"
---

# Blog Editor Skill

## When to use this skill

Use this skill when:
- the user asks to improve writing
- the user wants editing but says “don’t change my tone”
- the content is a blog, newsletter, or article draft
- the writing feels unclear, messy, or not impactful
- the user asks for better hooks, endings, or flow

Do NOT use this skill when:
- the user only wants grammar correction
- the task is factual rewriting or summarization only
- the user explicitly asks for a formal or academic rewrite

---

## Author’s writing style

The default voice this skill is built around:

> Conversational, insight-driven technical writing that explains simply, thinks out loud, and always lands on something actionable.

What that means in practice:

- **Conversational** — writes like a person talking, not a document explaining. Contractions, direct address, and natural sentence rhythm are all intentional.
- **Insight-driven** — every piece builds toward a point. There is a reason the piece exists, and the reader should feel it by the end.
- **Thinks out loud** — reasoning is shown, not just conclusions. The writer works through ideas with the reader, not at them.
- **Explains simply** — complex ideas are made clear without being dumbed down. Analogies and plain language are tools, not crutches.
- **Always actionable** — writing ends with something the reader can do, think differently about, or take away. No floating insights.

When editing, protect all of these. If an edit removes the conversational energy, makes the thinking invisible, or leaves the ending without direction — it is the wrong edit.

---

## What this skill does

This skill improves writing quality while preserving the author’s voice.

It focuses on:
- clarity
- structure
- readability
- impact

It does NOT:
- make writing sound generic
- over-formalize tone
- rewrite unnecessarily

---

## How to execute this skill

Follow this sequence:

### Step 1 — Understand intent
- Identify what the user wants:
  - light polish
  - deep rewrite
  - publish-ready edit

---

### Step 2 — Preserve voice
- Detect tone (conversational, reflective, technical)
- Keep sentence rhythm and personality intact
- Do NOT replace with generic phrasing

---

### Step 3 — Improve clarity
- Remove unnecessary words
- simplify sentences
- break long sentences into smaller ones

---

### Step 4 — Fix structure
- Ensure logical flow:
  - hook → context → explanation → insight → closing
- reorder sections if needed
- improve transitions

---

### Step 5 — Strengthen key sections

#### Hook
- make opening more engaging
- add curiosity or tension

#### Explanation
- simplify complex ideas
- add examples or analogies if needed

#### Insight / Closing
- sharpen key takeaway
- make final lines memorable

---

### Step 6 — Remove redundancy
- eliminate repeated ideas
- keep only intentional emphasis

---

### Step 7 — Improve readability
- break large paragraphs
- add spacing
- format for easy scanning

---

### Step 8 — Final authenticity check
Before returning output, verify against the author's style:
- does it still sound conversational, not formal or stiff?
- is the reasoning visible — does the writing think out loud or just state conclusions?
- is the explanation simple without being shallow?
- does it end on something actionable?
- did we remove personality? (if yes → fix)

---

## Output format

Return:

1. Edited version of the text

2. Short summary of improvements:
   - clarity
   - structure
   - tone preservation
   - impact

3. Optional suggestions (only if relevant):
   - improved hook
   - title ideas
   - teaser
   - stronger closing

---

## Editing modes

### light_edit
- minimal changes
- preserve original almost entirely

### deep_edit
- improve clarity and flow significantly
- restructure if needed

### publish_ready
- full pass including hook, structure, and formatting
- ready for publishing

---

## When to check references/examples.md

Check `references/example.md` at these specific points:

| When | Why |
|---|---|
| Rewriting a hook | See strong before/after examples to calibrate the right level of punch |
| Simplifying a sentence | See clarity transformations to know how much to cut |
| Rewriting an explanation | See how to use analogies without over-simplifying |
| Sharpening an insight or closing line | See punchline rewrites to match the right tone |
| Breaking up dense text | See formatting patterns to decide when and how to use lists |
| Unsure if an edit is too formal or generic | Check anti-patterns before returning output |

When in doubt about whether an edit fits the author's voice — check the examples before committing to it.

---

## Guardrails

- Do not over-edit
- Do not remove personality
- Do not introduce new information
- Do not make writing sound like generic AI output
- Prefer clarity over complexity
- Prefer natural phrasing over “perfect” phrasing