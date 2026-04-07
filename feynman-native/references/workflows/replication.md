# Replication

Use this workflow to plan or execute a reproduction of a paper's claim, benchmark, or experiment.

## Trigger phrases
- replicate this paper
- reproduce the results
- verify this claim empirically
- build a replication package
- can we reproduce this

## Deliverable
- Plan: `outputs/.plans/<slug>.md`
- Final report: `outputs/<slug>.md`
- Code and logs: `experiments/<slug>/`
- Provenance sidecar: `outputs/<slug>.provenance.md`

## Execution contract

### 1. Extract implementation details
Use the `researcher` role to pull:
- method, architecture, hyperparameters
- training / evaluation scripts
- dataset details
- environment requirements
- any linked code repo

### 2. Write a replication plan
Before running anything, specify:
- what claims or numbers will be checked
- what code / scripts are needed
- what datasets are required
- what environment is needed
- success oracle: how will we decide if it replicated or not

Save to `outputs/.plans/<slug>.md`.

### 3. Confirm execution environment
Ask the user which environment before running code:

| Option | Description |
|---|---|
| **Local** | run in the current working directory |
| **Virtual env** | create an isolated venv/conda env first |
| **Docker** | run inside an isolated container (see `tooling/docker.md` when available) |
| **Plan only** | produce the plan without executing |

Do not install packages, run training, or execute experiments without confirming the environment first.

### 4. Execute
If execution was approved:
- implement the scripts
- run them in the chosen environment
- capture all raw outputs
- save scripts, commands, outputs, and logs under `experiments/<slug>/`

### 5. Evaluate honestly
- compare actual results against the success oracle defined in the plan
- never call it replicated unless the planned checks actually passed
- record partial matches, failures, and deviations
- note any environmental differences from the original setup

### 6. Report
Write the final report to `outputs/<slug>.md` with:
- replication plan summary
- environment used
- results versus success oracle
- differences from original
- open questions
- Sources section

### 7. Provenance
Generate provenance sidecar.

## Minimum acceptance bar
- plan with explicit success oracle
- environment confirmed before execution
- honest pass/fail assessment
- no claiming replication without evidence
