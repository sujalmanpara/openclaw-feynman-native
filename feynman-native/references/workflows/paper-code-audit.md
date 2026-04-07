# Paper-Code Audit

Use this workflow to compare a paper's claims against its public codebase and identify mismatches, omissions, ambiguities, and reproducibility risks.

## Trigger phrases
- audit this paper
- compare the paper to the repo
- paper vs code
- does the implementation match the paper
- reproducibility audit

## Deliverable
- Final artifact: `outputs/<slug>-audit.md`
- Provenance sidecar: `outputs/<slug>-audit.provenance.md`
- Plan: `outputs/.plans/<slug>.md`
- Draft: `outputs/.drafts/<slug>-audit-draft.md`

## Execution contract

### 1. Plan first
Before broad inspection, write the audit plan with:
- paper URL / arXiv ID
- repo URL
- claims to check
- code areas likely to matter
- acceptance criteria for saying the claim matches, partially matches, or mismatches

### 2. Gather evidence from both sides
Use paper search / paper-reading tools for the paper and direct repo inspection for the code.
Suggested split:
- one evidence pass for paper claims and methodological details
- one evidence pass for repo structure, defaults, scripts, and metrics

### 3. Compare at the claim level
Check at minimum:
- method description vs implementation
- training/inference defaults
- metrics and benchmark handling
- dataset / preprocessing assumptions
- missing code paths or missing release artifacts
- reproduction blockers

### 4. Required output structure
```md
# Title

## Executive Summary

## Audit Scope

## Claim-by-Claim Comparison

## Mismatches and Omissions

## Reproducibility Risks

## Confidence and Open Questions

## Sources
```

### 5. Integrity rules
- Do not claim a mismatch unless you can point to the exact paper passage and the exact code path or missing artifact.
- Distinguish clearly between:
  - confirmed mismatch
  - likely mismatch
  - unresolved ambiguity
- If code is absent, say the claim is unverifiable, not false.

### 6. Verification loop
Run the verifier/reviewer loop before delivery for substantial audits.

## Minimum acceptance bar
- explicit paper and repo URLs
- at least one claim-level comparison table or section
- reproducibility risks called out separately
- confidence labels present
