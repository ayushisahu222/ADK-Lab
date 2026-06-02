# ADK Blog Editor

An AI-powered blog editor built with [Google ADK](https://google.github.io/adk-docs/). It improves writing quality while preserving the author's original voice — not a grammar fixer, but a full editorial pass that sharpens clarity, structure, and impact.

---

## What it does

The editor agent acts as an editor-in-chief. Give it a draft and it will:

- Preserve the author's conversational, insight-driven voice
- Improve clarity, structure, and flow
- Strengthen hooks and closing lines
- Remove redundancy without stripping personality
- Format content for readability
- Return an edited version with a short summary of changes

---

## How it works

The agent is built on Google ADK and uses a custom `editor-skills` skill set loaded from the `skills/` directory.

```
editor_agent/
├── agent.py              # Root agent definition
└── skills/
    └── editor-skills/
        ├── SKILL.md      # Skill instructions and editing steps
        └── references/
            └── example.md   # Before/after examples for hooks, clarity, explanations, insights, formatting, and anti-patterns
```

The agent uses `gemini-2.5-flash` and follows a structured 8-step editing process defined in `SKILL.md`.

---