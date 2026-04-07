---
name: feynman-native
description: Native OpenClaw research system modeled after Feynman. Use when the user asks for deep research, literature reviews, paper surveys, source comparisons, peer review, paper-vs-code audits, research drafts, replication plans, autonomous experiment loops, or recurring research watches with citations and provenance.
---

# Feynman Native

Build source-grounded research artifacts inside OpenClaw with plan-first execution, explicit verification, durable outputs, and role-based subagent orchestration.

## Quick routing

Read `references/workflows.md` first, then load the dedicated workflow file:

- **Deep research / comprehensive analysis / in-depth report** → `references/workflows/deepresearch.md`
- **Lit review / state of the art / paper survey** → `references/workflows/literature-review.md`
- **Compare tools, papers, approaches, or claims** → `references/workflows/source-comparison.md`
- **Review a draft, paper, memo, or benchmark writeup** → `references/workflows/peer-review.md`
- **Check paper claims against code** → `references/workflows/paper-code-audit.md`
- **Turn research into a polished draft** → `references/workflows/draft-writing.md`
- **Replicate or reproduce a result** → `references/workflows/replication.md`
- **Run an iterative experiment loop** → `references/workflows/autoresearch.md`
- **Monitor a topic over time** → `references/workflows/watch.md`
- **Explain something simply / ELI5** → `references/workflows/eli5.md`
- **Any substantial draft that needs citations + stress testing** → `references/workflows/verification-loop.md`
- **Log session progress** → `references/workflows/session-log.md`
- **Recover prior research context** → `references/workflows/session-search.md`
- **Check active background work** → `references/workflows/jobs.md`

Read `references/tooling/paper-search.md` whenever academic paper discovery is central and exact alphaXiv parity is not available.
Read `references/agents.md` before spawning role-based subagents.
Read `references/parity-matrix.md` when extending the skill, checking what still lacks parity, or deciding whether a Feynman-specific feature needs an adapter.

## Operating contract

- Start with a **plan artifact** for any non-trivial research job.
- Use one **canonical final Markdown artifact** per user-facing job.
- Save durable artifacts under:
  - `outputs/` for research briefs, reviews, comparisons, audits, and summaries
  - `papers/` for paper-style drafts
  - `experiments/` for runnable experiments and logs
  - `notes/` for scratch notes and intermediate synthesis
  - `outputs/.plans/` for plan files
  - `outputs/.drafts/` for pre-citation drafts
- Produce a provenance sidecar next to the final artifact.
- Prefer direct URLs for every source. Never cite a source you did not inspect closely enough to support the claim.
- Never say `verified`, `confirmed`, or `reproduced` unless the check actually happened and the evidence is recorded.
- For current topics, use web sources first. For academic topics, use paper search first. For mixed topics, use both.
- Use subagents only when decomposition reduces context pressure or meaningfully improves coverage.

## Default execution pattern

1. Derive a short slug using `scripts/make_slug.py`.
2. Initialize output scaffolding with `scripts/init_artifact.py` when helpful.
3. Write a plan with:
   - key questions
   - evidence types needed
   - acceptance criteria
   - task ledger
   - verification log
4. Present the plan and get confirmation before major work.
5. Gather evidence directly or with `researcher` subagents.
6. Synthesize into a draft yourself unless a workflow explicitly benefits from the `writer` role.
7. Run `verifier` and `reviewer` passes before delivery when the artifact is substantial.
8. Save the final artifact plus provenance.

## Role model

Use these role definitions from `references/agents.md`:

- **researcher** — gather evidence across web, papers, docs, repos, and local artifacts
- **writer** — turn evidence into a readable draft without outrunning the sources
- **verifier** — add citations, verify URLs, and remove unsupported claims
- **reviewer** — adversarially pressure-test logic, rigor, and confidence

## Helper scripts

- `scripts/make_slug.py` — normalize a topic into a short slug
- `scripts/init_artifact.py` — create standard folders and a starter plan file
- `scripts/merge_sources.py` — deduplicate URLs across research files into a unified source inventory
- `scripts/verify_urls.py` — check URL liveness for draft/research files
- `scripts/build_provenance.py` — generate a provenance sidecar for the final artifact
- `scripts/paper_search.py` — arXiv-first paper discovery helper for native paper search

## Current stage

This skill now has **full workflow parity** with Feynman:
- deep research, literature review, source comparison, peer review
- paper-code audit, draft writing
- replication, autoresearch, watch
- ELI5, session log, session search, jobs/status
- verification/provenance loop
- native paper-search adapter path

Next milestone should target optional ecosystem adapters (Docker polish, Modal, RunPod, preview/export).
