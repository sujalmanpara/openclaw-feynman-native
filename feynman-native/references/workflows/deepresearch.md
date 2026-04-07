# Deep Research

Use this workflow for broad, source-heavy investigations that need planning, parallel evidence gathering, synthesis, citation, and verification.

## Trigger phrases
- deep research
- comprehensive analysis
- in-depth report
- investigate this thoroughly
- source-heavy research brief

## Deliverable
- Final artifact: `outputs/<slug>.md`
- Provenance sidecar: `outputs/<slug>.provenance.md`
- Plan: `outputs/.plans/<slug>.md`
- Draft: `outputs/.drafts/<slug>-draft.md`

## Execution contract

### 1. Plan first
- Derive slug with `scripts/make_slug.py`.
- Create plan scaffold with `scripts/init_artifact.py`.
- In the plan file, fill in:
  - key questions
  - source types needed
  - research dimensions worth parallelizing
  - acceptance criteria
  - task ledger
  - verification log
- Present the plan before broad execution.

### 2. Decide scale
Use this table:

| Topic size | Strategy |
|---|---|
| narrow factual question | no subagents, search directly |
| comparison of 2-3 items | 2 researcher passes |
| broad topic with multiple dimensions | 3-4 researcher passes |
| large multi-domain topic | 4-6 researcher passes |

Never spawn subagents for work you can finish in ~5 direct tool calls.

### 3. Gather evidence
Assign disjoint dimensions only. Good partitioning axes:
- academic papers
- official docs / vendor pages
- public code / repos
- benchmarks / datasets
- geography / timeframe splits

Each `researcher` run must produce:
- evidence table
- findings with inline source refs like `[1]`
- numbered Sources section
- Coverage Status

Suggested output names:
- `notes/<slug>-research-papers.md`
- `notes/<slug>-research-web.md`
- `notes/<slug>-research-repos.md`
- `notes/<slug>-research-benchmarks.md`

### 4. Evaluate and loop
After each batch:
- read the returned research files
- update the task ledger
- mark unanswered questions
- identify single-source critical claims
- resolve contradictions or launch one more targeted batch

Stop only when:
- all material questions are answered, or
- the remaining uncertainty is explicit and acceptable

### 5. Draft the report
Write the draft yourself unless context pressure is high enough to justify a `writer` pass.

Required structure:
```md
# Title

## Executive Summary

## Key Findings

## Evidence by Theme

## Disagreements / Gaps

## Open Questions

## Recommended Next Steps
```

Rules:
- separate observations from inferences
- label single-source critical findings
- do not claim verification unless the verification log supports it

Save to `outputs/.drafts/<slug>-draft.md`.

### 6. Verify citations and URLs
Run the verification loop in `verification-loop.md`.
- verifier pass anchors claims to sources
- reviewer pass stress-tests unsupported claims and confidence levels

### 7. Deliver
- save final artifact to `outputs/<slug>.md`
- generate provenance with `scripts/build_provenance.py`
- include direct URLs in Sources

## Minimum acceptance bar
- ≥5 direct sources unless the topic is inherently narrow
- no critical unsupported claims
- no orphan citations or orphan sources
- explicit disagreement/gap section when evidence is mixed
