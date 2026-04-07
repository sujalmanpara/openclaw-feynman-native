# Research Plan: Feynman Native core parity

- **Slug:** `feynman-native-core-parity`
- **Created:** 2026-04-07 10:02 UTC

## Questions
1. How should deep research, literature review, comparison, and review flows be encoded so OpenClaw can execute them natively without guessing?
2. What helper scripts are needed to support the verifier/reviewer loop and provenance discipline?
3. What parts of milestone 2 can be considered operational now, and what remains for later milestones?

## Strategy
- Split milestone 2 into workflow-specific reference files instead of one generic document.
- Make the verification loop explicit so all substantial artifacts follow the same citation/review path.
- Add small deterministic scripts for source merging, URL checking, and provenance generation.
- Re-validate the skill after the new core layer is added.

## Acceptance Criteria
- [x] Deep research workflow reference written
- [x] Literature review workflow reference written
- [x] Source comparison workflow reference written
- [x] Peer review workflow reference written
- [x] Verification loop reference written
- [x] `merge_sources.py` implemented and tested
- [x] `verify_urls.py` implemented and tested
- [x] `build_provenance.py` implemented and tested
- [x] Skill validates cleanly
- [ ] Milestone 3 workflows implemented

## Task Ledger
| ID | Owner | Task | Status | Output |
|---|---|---|---|---|
| T1 | lead | Create plan | done | `outputs/.plans/feynman-native-core-parity.md` |
| T2 | lead | Implement deep research workflow ref | done | `references/workflows/deepresearch.md` |
| T3 | lead | Implement literature review workflow ref | done | `references/workflows/literature-review.md` |
| T4 | lead | Implement source comparison workflow ref | done | `references/workflows/source-comparison.md` |
| T5 | lead | Implement peer review workflow ref | done | `references/workflows/peer-review.md` |
| T6 | lead | Implement verification loop ref | done | `references/workflows/verification-loop.md` |
| T7 | lead | Implement URL/source/provenance scripts | done | `scripts/merge_sources.py`, `scripts/verify_urls.py`, `scripts/build_provenance.py` |
| T8 | lead | Re-validate skill | done | validator output |
| T9 | lead | Implement audit/draft workflows | todo | pending |

## Verification Log
| Item | Method | Status | Evidence |
|---|---|---|---|
| `merge_sources.py` behavior | direct execution | done | `/tmp/unified-sources.md` |
| `verify_urls.py` behavior | direct execution | done | `/tmp/url-check.md` |
| `build_provenance.py` behavior | direct execution | done | `/tmp/provenance.md` |
| Skill validity | validator run | done | `Skill is valid!` |

## Decision Log
- Milestone 2 is implemented as a reusable operating layer, not a one-off research prompt.
- Verification/provenance support is built as scripts so later workflows can reuse it.
- Paper-code audit and draft-writing are the next logical milestone because they depend on the same verification loop.
