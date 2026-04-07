# Session Search

Use this workflow to recover prior research work, findings, and context from past sessions.

## Trigger phrases
- what did we do before
- find our previous research on X
- search past sessions
- recover prior context

## How it works in OpenClaw

OpenClaw does not use Feynman's JSONL session transcripts. Instead, search:

1. **Research artifacts** — `outputs/`, `papers/`, `notes/`, `experiments/`
2. **Plan files** — `outputs/.plans/`
3. **Memory** — use `memory_search` for prior preferences, decisions, and lessons
4. **Daily memory files** — `memory/YYYY-MM-DD.md`

## Search strategy

1. Search artifact directories first:
   ```bash
   grep -ril "<query>" outputs/ papers/ notes/ experiments/
   ```

2. If not found in artifacts, search memory and daily files.

3. If still not found, inform the user that no prior context was found and offer to start fresh.

## Output
Return a concise summary of what was found, with file paths and relevant excerpts.
