# ELI5

Use this workflow to explain research, papers, or technical ideas in plain English.

## Trigger phrases
- ELI5 this
- explain this simply
- what does this paper actually mean
- remove the jargon
- plain English version

## Execution contract

### 1. Identify the source
- If the user names a specific paper or arXiv ID, fetch and read it first.
- If the user gives only a topic, identify 1-3 representative papers and anchor the explanation around the clearest one.

### 2. Required structure
```md
## One-Sentence Summary

## Big Idea

## How It Works

## Why It Matters

## What To Be Skeptical Of

## If You Remember 3 Things
```

### 3. Rules
- Use short sentences and concrete words.
- Define jargon immediately or remove it.
- Prefer one good analogy over several weak ones.
- Separate what the paper actually shows from speculation or interpretation.
- Keep the explanation inline unless the user explicitly asks to save it as an artifact.

## Output
Inline response by default. Save to `outputs/<slug>-eli5.md` only if the user asks.
