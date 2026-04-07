# Research Plan: Feynman Native research product parity

- **Slug:** `feynman-native-research-product-parity`
- **Created:** 2026-04-07 10:12 UTC

## Questions
1. How should paper-code audit and draft-writing be expressed natively so they match Feynman's workflow expectations?
2. How should verifier/reviewer rules be strengthened so later workflows inherit stricter evidence discipline?
3. What paper-search adapter path gives strong native behavior without depending on alpha CLI?

## Strategy
- Add dedicated workflow references for paper-code audit and draft writing.
- Strengthen the shared agent contracts, especially verifier and reviewer rules.
- Add an explicit paper-search adapter document plus a tiny arXiv-first helper script.
- Re-validate the skill after smoke-testing the paper search script.

## Acceptance Criteria
- [x] Paper-code audit workflow reference written
- [x] Draft-writing workflow reference written
- [x] Paper-search adapter reference written
- [x] Native paper search helper implemented and tested
- [x] Verifier/reviewer rules hardened
- [x] Skill validates cleanly
- [ ] Replication / autoresearch / watch workflows implemented

## Task Ledger
| ID | Owner | Task | Status | Output |
|---|---|---|---|---|
| T1 | lead | Create plan | done | `outputs/.plans/feynman-native-research-product-parity.md` |
| T2 | lead | Implement paper-code audit workflow | done | `references/workflows/paper-code-audit.md` |
| T3 | lead | Implement draft-writing workflow | done | `references/workflows/draft-writing.md` |
| T4 | lead | Implement paper-search adapter path | done | `references/tooling/paper-search.md` |
| T5 | lead | Build native paper-search helper | done | `scripts/paper_search.py` |
| T6 | lead | Harden verifier/reviewer rules | done | `references/agents.md` |
| T7 | lead | Re-validate skill | done | validator output |
| T8 | lead | Implement replication/autoresearch/watch | todo | pending |

## Verification Log
| Item | Method | Status | Evidence |
|---|---|---|---|
| `paper_search.py` behavior | direct execution | done | `/tmp/paper-search.md` |
| Skill validity | validator run | done | `Skill is valid!` |

## Decision Log
- Native paper search is implemented as an arXiv-first helper plus web/repo follow-up, not as a hard alphaXiv dependency.
- Audit and draft-writing are now first-class workflows instead of vague future placeholders.
- The next implementation milestone should focus on replication, autoresearch, and watch flows.
