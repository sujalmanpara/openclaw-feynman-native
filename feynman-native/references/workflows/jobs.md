# Jobs

Use this workflow to inspect active background research work, scheduled follow-ups, and pending tasks.

## Trigger phrases
- what's running
- check background work
- show active jobs
- research status

## How it works in OpenClaw

Map Feynman's jobs surface to OpenClaw equivalents:

1. **Running processes** — use `process` tool with `list` action
2. **Active subagents** — use `subagents` tool with `list` action
3. **Scheduled tasks** — check cron jobs or heartbeat config
4. **Watch jobs** — check `outputs/.plans/` for active watch plans

## Output format
```md
## Active Background Work

### Running Processes
- [list or "none"]

### Active Subagents
- [list or "none"]

### Scheduled / Recurring Jobs
- [list or "none"]

### Failures Needing Attention
- [list or "none"]

### Next Steps
- [what the user should do if they want details]
```

Keep it concise and operational.
