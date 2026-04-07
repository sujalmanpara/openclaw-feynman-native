# Feynman Native Workflow Index

Use this file as the routing table. After choosing a workflow, read the dedicated file for the full execution contract.

## All workflows

### Research workflows
- **Deep Research** → `workflows/deepresearch.md`
- **Literature Review** → `workflows/literature-review.md`
- **Source Comparison** → `workflows/source-comparison.md`
- **Peer Review** → `workflows/peer-review.md`
- **Paper-Code Audit** → `workflows/paper-code-audit.md`
- **Draft Writing** → `workflows/draft-writing.md`
- **Replication** → `workflows/replication.md`
- **Autoresearch** → `workflows/autoresearch.md`
- **Watch** → `workflows/watch.md`
- **ELI5** → `workflows/eli5.md`

### Operational workflows
- **Verification Loop** → `workflows/verification-loop.md`
- **Session Log** → `workflows/session-log.md`
- **Session Search** → `workflows/session-search.md`
- **Jobs / Status** → `workflows/jobs.md`

## Shared artifact conventions

- `outputs/<slug>.md` — final non-paper artifact
- `papers/<slug>.md` — final paper-style artifact
- `outputs/<slug>.provenance.md` — provenance sidecar
- `outputs/.plans/<slug>.md` — plan artifact
- `outputs/.drafts/<slug>-draft.md` — uncited draft
- `notes/<slug>-*.md` — intermediate research / review files
- `experiments/<slug>/` — experiment code and logs

## Shared operating rules

1. Plan first for non-trivial work.
2. Use one canonical final artifact.
3. Prefer direct URLs for every source.
4. Never claim verification or reproduction without recorded evidence.
5. Run the verification loop on substantial outputs.
