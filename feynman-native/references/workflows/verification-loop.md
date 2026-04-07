# Verification Loop

Use this loop whenever a substantial draft needs citations, URL checks, and an adversarial pass before delivery.

## Goal
Turn an evidence-grounded draft into a cited, checked, and pressure-tested final artifact.

## Inputs
- draft file
- one or more research/evidence files
- final output path
- review output path

## Step 1 — verifier pass
Use the `verifier` role to:
- add inline citations
- unify and renumber sources
- verify every URL
- remove or weaken unsupported claims
- build the Sources section

Suggested output:
- final draft candidate at `outputs/<slug>.md`

### Useful helpers
- `scripts/merge_sources.py` to deduplicate and inventory URLs across research files
- `scripts/verify_urls.py` to pre-check URL liveness

## Step 2 — reviewer pass
Use the `reviewer` role in **verification-style audit** mode to check:
- unsupported claims that slipped through
- confidence stronger than evidence quality
- contradictions between sections
- single-source critical findings
- zombie paragraphs that no longer match the evidence

Suggested output:
- `notes/<slug>-review.md`

## Step 3 — fix / escalate
- Fix any fatal issue before delivery.
- Note major issues in the final artifact if they remain unresolved.
- If fatal issues were found, run one more review-style pass after fixing them.

## Step 4 — provenance
Generate provenance with `scripts/build_provenance.py`.

## Minimum exit criteria
- final artifact exists
- provenance sidecar exists
- no fatal reviewer issues remain
- final Sources section uses direct URLs
