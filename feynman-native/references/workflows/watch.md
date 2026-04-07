# Watch

Use this workflow for recurring or deferred research monitoring of a topic, company, paper area, or product surface.

## Trigger phrases
- watch this topic
- monitor this field
- track new papers on X
- set up alerts for Y
- keep an eye on Z

## Deliverable
- Baseline: `outputs/<slug>-baseline.md`
- Plan: `outputs/.plans/<slug>.md`
- Follow-up artifacts as future sweeps happen
- Provenance sidecar: `outputs/<slug>-baseline.provenance.md`

## Execution contract

### 1. Plan the watch
Before gathering, define:
- what to monitor (topic, company, product, paper area)
- what signals count as meaningful change
- check frequency (daily, weekly, on-demand)
- comparison method (diff against baseline)

Save to `outputs/.plans/<slug>.md`.

### 2. Run a baseline sweep
Use the `researcher` role to gather the current state of the topic.
Save to `outputs/<slug>-baseline.md` with full source links.

### 3. Schedule follow-ups
Use OpenClaw's scheduling capabilities:
- **cron jobs** for recurring checks at fixed intervals
- **heartbeat tasks** for lower-frequency monitoring
- **manual re-runs** if the user prefers on-demand checks

The scheduled task should:
1. re-run the researcher pass
2. compare new findings against the baseline
3. generate a diff or changelog
4. notify only when there is a material change (unless the user asked for every run)

### 4. Follow-up artifact format
```md
# Watch Update: [topic]

## Date: [date]

## Changes Since Baseline
- [change 1]
- [change 2]

## No Change
- [areas that remain the same]

## New Sources
- [source 1]
- [source 2]

## Assessment
[Is the change material enough to act on?]
```

Save follow-ups as `outputs/<slug>-update-YYYY-MM-DD.md`.

### 5. Baseline refresh
When the accumulated changes are large enough, offer to refresh the baseline by creating a new one and archiving the old.

## Minimum acceptance bar
- explicit watch plan with signals defined
- baseline artifact with source URLs
- scheduling mechanism set up or documented
- follow-up format defined
