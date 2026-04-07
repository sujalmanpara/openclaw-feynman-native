# Literature Review

Use this workflow for paper surveys, state-of-the-art summaries, academic landscape maps, or "what does the literature say" requests.

## Trigger phrases
- lit review
- literature review
- paper survey
- state of the art
- academic landscape

## Deliverable
- Final artifact: `outputs/<slug>.md`
- Provenance sidecar: `outputs/<slug>.provenance.md`
- Plan: `outputs/.plans/<slug>.md`
- Draft: `outputs/.drafts/<slug>-draft.md`

## Execution contract

### 1. Plan the scope
Before gathering, define:
- exact topic boundary
- relevant years / period
- paper types that count (core methods, benchmarks, surveys, critiques)
- key questions
- what would count as consensus vs disagreement

### 2. Gather paper-first evidence
Prefer paper and official repo sources first.
Supplement with docs or benchmark pages only when they clarify implementation or recency.

If the sweep is broad, split researchers by:
- time period
- subfield / method family
- evaluation / benchmark angle
- theory vs systems vs application angle

### 3. Synthesize like a real lit review
Required sections:
```md
# Title

## Executive Summary

## Scope and Method

## Consensus

## Disagreements

## Method Families / Approaches

## Limitations in the Literature

## Open Questions

## Suggested Reading / Next Experiments
```

### 4. Integrity rules
- Never describe a paper beyond what you actually inspected.
- Distinguish paper claims from reproduced or benchmarked reality.
- Avoid turning one flashy paper into field consensus.
- If literature is thin, say it plainly.

### 5. Verification loop
Run the verifier/reviewer loop before delivery.

## Minimum acceptance bar
- explicit scope section
- explicit consensus/disagreement separation
- paper-level URLs in Sources
- uncertainty surfaced, not flattened
