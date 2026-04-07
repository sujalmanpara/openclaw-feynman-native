# Feynman Native Parity Matrix

This file maps the current Feynman repository to the native OpenClaw implementation target.

## Scope

Target:
- **100% workflow parity**
- **Near-100% capability parity** where OpenClaw supports the required tools
- **Optional adapter parity** for ecosystem-specific dependencies such as alphaXiv, Modal, or RunPod

Non-goal for milestone 1:
- exact CLI parity
- exact Pi runtime parity
- exact package/runtime identity

---

## Source inventory reverse-engineered in step 1

### Top-level Feynman surfaces
- CLI entrypoint: `src/cli.ts`, `src/index.ts`, `bin/feynman.js`
- Global system prompt: `.feynman/SYSTEM.md`
- Prompt workflows: `prompts/*.md`
- Packaged skills: `skills/*/SKILL.md`
- Role agents: `.feynman/agents/*.md`
- Command metadata: `metadata/commands.mjs`
- Extensions/tool adapters: `extensions/research-tools.ts`, `.feynman/vendor-overrides/...`

### Workflow prompts discovered
- `deepresearch`
- `lit`
- `review`
- `audit`
- `compare`
- `draft`
- `replicate`
- `autoresearch`
- `watch`
- plus operational helpers: `jobs`, `log`

### Role agents discovered
- `researcher`
- `writer`
- `verifier`
- `reviewer`

---

## Workflow parity

| Feynman workflow | Native OpenClaw target | Status | Notes |
|---|---|---:|---|
| deepresearch | plan-first orchestration with researcher/verifier/reviewer passes | core-ready | dedicated workflow + helper scripts added |
| lit | literature review flow with paper-first evidence | core-ready | dedicated workflow + helper scripts added |
| review | adversarial review / verification pass | core-ready | dedicated workflow + helper scripts added |
| audit | paper-vs-code audit workflow | core-ready | dedicated workflow added |
| compare | grounded comparison matrix | core-ready | dedicated workflow + helper scripts added |
| draft | paper-style or memo-style writeup from evidence | core-ready | dedicated workflow added |
| replicate | replication planning + execution environments | core-ready | dedicated workflow added |
| autoresearch | iterative experiment loop | core-ready | dedicated workflow added |
| watch | recurring monitor with baseline + scheduled follow-up | core-ready | dedicated workflow added |
| jobs | inspect running background work | core-ready | mapped to OpenClaw process/session/cron tools |
| log | durable session log | core-ready | dedicated workflow added |
| eli5 | plain-English research explanation | core-ready | dedicated workflow added |
| session-search | recover prior research context | core-ready | mapped to artifact + memory search |

---

## Agent parity

| Feynman role | Native OpenClaw role | Status | Notes |
|---|---|---:|---|
| researcher | subagent/self-pass following evidence-table contract | skeleton | defined in `references/agents.md` |
| writer | drafting pass from supplied evidence only | skeleton | defined |
| verifier | citation + URL verification pass | skeleton | defined |
| reviewer | skeptical audit / peer review pass | skeleton | defined |

---

## Tool and dependency parity

| Feynman dependency | Native plan | Status | Gap handling |
|---|---|---:|---|
| alpha CLI / alphaXiv | native paper search + arXiv/official repo search + optional adapter | partial | `paper_search.py` + adapter strategy documented; exact alpha parity still optional |
| web search | OpenClaw `web_search` + `web_fetch` | strong | available now |
| session search | search prior outputs/notes + memory facilities | partial | implement helper/index later |
| Docker | OpenClaw exec + local Docker if installed | partial | environment-dependent |
| Modal | optional external CLI integration | gap | later milestone |
| RunPod | optional external CLI integration | gap | later milestone |
| preview / PDF export | OpenClaw-compatible preview/export path | gap | later milestone |
| package-based memory | OpenClaw memory + file artifacts | partial | strong enough for workflow parity |
| Pi subagents | OpenClaw subagents | strong | available now |

---

## Output parity

| Feynman artifact | Native target | Status |
|---|---|---:|
| `outputs/.plans/<slug>.md` | same | ready |
| `outputs/.drafts/<slug>-draft.md` | same | ready |
| `outputs/<slug>.md` | same | ready |
| `papers/<slug>.md` | same | ready |
| `outputs/<slug>.provenance.md` | same | ready |
| `experiments/<slug>/...` | same | ready |
| `notes/<slug>-*.md` | same | ready |

---

## Milestone plan

### Milestone 1 — completed in skeleton form
- reverse-engineer repository structure
- create native skill skeleton
- create workflow map
- create agent map
- create parity matrix
- create helper scripts for slugging + artifact init

### Milestone 2 — core parity
- implement deepresearch
- implement literature review
- implement source comparison
- implement peer review
- implement citation/provenance pass
- **Status:** core workflow references + helper scripts completed

### Milestone 3 — research product parity
- implement paper-code audit
- implement draft workflow
- harden verification rules
- add optional paper-search adapter path
- **Status:** core milestone completed for audit/draft/adapter scaffolding

### Milestone 4 — advanced parity
- replication planning + at least one execution mode
- autoresearch loop
- watch scheduling
- jobs/status surface
- ELI5, session log, session search
- **Status:** all workflow references completed

### Milestone 5 — optional ecosystem parity
- alpha adapter
- Docker polish
- Modal adapter
- RunPod adapter
- preview/export layer

---

## Critical gaps to solve later

1. **Paper search parity**
   - Feynman leans on alphaXiv/alpha CLI.
   - Native OpenClaw needs either an adapter or a robust replacement path.

2. **Exact compute parity**
   - Replication, Modal, and RunPod support depend on local environment and external CLIs.

3. **Jobs/status UX parity**
   - Feynman has a jobs/status surface; native OpenClaw needs a clean equivalent.

4. **Preview/export parity**
   - Browser/PDF preview needs explicit implementation if we want feature parity, not just workflow parity.

---

## Milestone-1 verdict

The repo has been decomposed into:
- workflows
- role agents
- dependency surfaces
- artifact conventions

This is enough to begin **native implementation without guessing**.
**All Feynman workflows now have dedicated native references.**
The next coding phase should target **optional ecosystem adapters** (Docker, Modal, RunPod, preview/export) and live end-to-end testing.
