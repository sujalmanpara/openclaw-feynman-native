# Draft Writing

Use this workflow to turn already-collected research findings into a polished paper-style or memo-style draft.

## Trigger phrases
- write a paper draft
- turn this research into a report
- draft a technical memo
- paper-style writeup
- write up these findings

## Deliverable
- Final artifact: `papers/<slug>.md` for paper-style output, otherwise `outputs/<slug>.md`
- Provenance sidecar next to the final artifact
- Plan: `outputs/.plans/<slug>.md`
- Optional intermediate draft: `outputs/.drafts/<slug>-draft.md`

## Execution contract

### 1. Outline before writing
Create a plan that includes:
- proposed title
- target output style
- sections
- key claims
- source material to draw from
- verification log for critical claims, figures, and calculations

### 2. Draft from evidence only
Use the `writer` role when that reduces context pressure.
Minimum paper-style sections:
- title
- abstract / executive summary
- problem statement
- related work or context
- method / synthesis
- evidence / experiments
- limitations
- conclusion

### 3. Visuals
Use charts, tables, or Mermaid only when they materially help understanding.
Every figure needs a caption and traceable underlying evidence.

### 4. Integrity rules
- Keep tentative results tentative.
- Remove unsupported numerics rather than hoping the verifier catches them later.
- Preserve disagreements and unresolved questions.
- Do not add fake citations during drafting if a later verification pass will handle them.

### 5. Verification loop
Run the verifier/reviewer loop before delivery unless the user explicitly asked for a rough draft only.

## Minimum acceptance bar
- outline written first
- explicit limitations section
- no strong claim without an obvious evidence home
- final artifact + provenance sidecar saved
