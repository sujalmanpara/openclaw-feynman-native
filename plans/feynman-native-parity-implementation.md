# Research Plan: Feynman Native parity implementation

- **Slug:** `feynman-native-parity-implementation`
- **Created:** 2026-04-07 09:53 UTC

## Questions
1. Which Feynman workflows, roles, artifacts, and tool surfaces must be reproduced for real parity?
2. Which parts can be implemented natively in OpenClaw immediately, and which require adapters or environment-dependent integrations?
3. What is the smallest native skill skeleton that preserves Feynman's operating model without guessing?

## Strategy
- Reverse-engineer the Feynman repo into four layers: workflows, agents, dependencies, and artifact conventions.
- Build a native OpenClaw skill skeleton that mirrors that structure while staying lean.
- Encode the execution rules in references files instead of bloating `SKILL.md`.
- Create helper scripts for slugging and artifact initialization so future workflows follow a consistent contract.
- Validate the skill structure before moving to milestone 2.

## Acceptance Criteria
- [x] Feynman workflows mapped into a native parity matrix
- [x] Native skill skeleton created under `skills/feynman-native/`
- [x] Role definitions and workflow blueprint written as references
- [x] Helper scripts created and tested
- [x] Skill validates cleanly
- [ ] Milestone 2 core workflows implemented

## Task Ledger
| ID | Owner | Task | Status | Output |
|---|---|---|---|---|
| T1 | lead | Reverse-engineer repo structure and surfaces | done | `skills/feynman-native/references/parity-matrix.md` |
| T2 | lead | Create native skill skeleton | done | `skills/feynman-native/SKILL.md` |
| T3 | lead | Define workflow blueprint | done | `skills/feynman-native/references/workflows.md` |
| T4 | lead | Define role contracts | done | `skills/feynman-native/references/agents.md` |
| T5 | lead | Build helper scripts | done | `skills/feynman-native/scripts/*.py` |
| T6 | lead | Validate skill structure | done | `quick_validate.py` output |
| T7 | lead | Implement milestone 2 core workflows | todo | pending |

## Verification Log
| Item | Method | Status | Evidence |
|---|---|---|---|
| Prompt/workflow inventory | direct repo inspection | done | `feynman-repo/prompts/*.md` |
| Role-agent inventory | direct repo inspection | done | `feynman-repo/.feynman/agents/*.md` |
| CLI/metadata surface | direct repo inspection | done | `feynman-repo/package.json`, `metadata/commands.mjs` |
| Skill skeleton validity | validator run | done | `Skill is valid!` |
| Helper script behavior | direct execution | done | slug + plan init outputs |

## Decision Log
- Milestone 1 targets workflow parity mapping and skeleton creation only; no false promise of exact runtime parity.
- Exact alphaXiv / Modal / RunPod parity is deferred behind native workflow implementation.
- Milestone 2 should start with `deepresearch`, `literature review`, `source comparison`, and the verifier/reviewer loop.
