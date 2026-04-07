# Paper Search Adapter Path

This file defines the native OpenClaw replacement path for Feynman's alphaXiv-heavy paper search behavior.

## Goal
Achieve workflow parity even when the exact Feynman `alpha` CLI is not installed.

## Strategy

### Tier 1 — native paper search
Use the bundled `scripts/paper_search.py` helper for arXiv-first discovery.
Use web search for:
- official paper pages
- project pages
- code repos
- benchmark sites
- author pages

### Tier 2 — direct repo and web inspection
After finding a paper candidate:
- inspect the arXiv/official paper URL
- inspect the linked repo or project page
- inspect benchmark or dataset pages when needed

### Tier 3 — optional alpha adapter
If the environment later gains alpha CLI access, prefer it for:
- semantic paper search
- paper Q&A
- repository reading attached to papers
- annotations

But do not make native workflows depend on alpha.

## Default native search pattern
1. Use `scripts/paper_search.py "<topic>"` for an arXiv-first shortlist.
2. Use web search to confirm recency, project pages, repos, benchmarks, and official docs.
3. Save the shortlist to a research note before deeper reading.
4. Read the top candidates directly before making claims.

## Rules
- Never answer a current-state question from paper search alone.
- Never infer paper content from title only when direct reading is available.
- Treat paper search as discovery, not proof.
