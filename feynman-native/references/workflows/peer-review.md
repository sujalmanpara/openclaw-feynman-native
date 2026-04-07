# Peer Review

Use this workflow for adversarial critique of a draft, paper, benchmark report, memo, or technical artifact.

## Trigger phrases
- review this draft
- peer review this
- critique this paper
- pressure test this writeup
- verify this report

## Deliverable
- Final review: `outputs/<slug>.md`
- Provenance sidecar: `outputs/<slug>.provenance.md`

## Execution contract

### 1. Determine review mode
Choose one and state it:
- **venue-style review** — novelty, clarity, empirical rigor, likely reviewer pushback
- **verification-style audit** — unsupported claims, weak citations, logical gaps, confidence mismatch

### 2. Inspect the artifact directly
Do not review a summary of the artifact when the artifact itself is available.
Quote exact passages when criticizing them.

### 3. Required output structure
```md
## Summary

## Strengths

## Weaknesses
- fatal
- major
- minor

## Questions for Authors

## Verdict

## Revision Plan

## Inline Annotations
```

### 4. Rules
- Every major criticism must point to a specific passage or section.
- Keep looking after the first issue.
- If the document might pass depending on venue norms, say so explicitly.
- For verification-style audits, prioritize evidence integrity over novelty commentary.

### 5. Optional citation check
If the artifact contains source-backed claims, run the verifier loop as part of the review.

## Minimum acceptance bar
- at least one quoted annotation for each major/fatal issue
- concrete revision plan
- clear severity labels
