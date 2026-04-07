# OpenClaw Feynman Native

Native OpenClaw research skill with full workflow parity to the [Feynman](https://github.com/getcompanion-ai/feynman) project.

## What this is

A portable OpenClaw skill that provides:
- **13 research workflows** — deep research, literature review, source comparison, peer review, paper-code audit, draft writing, replication, autoresearch, watch, ELI5, session log, session search, jobs/status
- **4 agent roles** — researcher, writer, verifier, reviewer
- **6 helper scripts** — slug generation, artifact init, source merging, URL verification, provenance generation, arXiv paper search
- **5 tooling adapters** — paper search, Docker, Modal, RunPod, preview/export
- **Verification loop** — citation anchoring, URL checking, adversarial review, provenance tracking

## Status: Full Parity ✅

Every Feynman workflow, agent role, artifact convention, and ecosystem adapter has a native OpenClaw equivalent.

## Repo structure

```
feynman-native/
  SKILL.md                          # skill entry point
  references/
    agents.md                       # 4 role definitions
    parity-matrix.md                # feature parity tracker
    workflows.md                    # workflow index
    workflows/                      # 13 dedicated workflow refs
    tooling/                        # 5 adapter docs
  scripts/
    make_slug.py                    # topic → slug
    init_artifact.py                # scaffold outputs/plans
    merge_sources.py                # deduplicate URLs
    verify_urls.py                  # check URL liveness
    build_provenance.py             # generate provenance sidecar
    paper_search.py                 # arXiv API search
plans/                              # milestone planning artifacts
```

## Usage

Copy or symlink the `feynman-native/` folder into your OpenClaw skills directory:

```bash
cp -R feynman-native ~/.openclaw/workspace/skills/
```

The skill auto-triggers on research-related requests.

## License

MIT
