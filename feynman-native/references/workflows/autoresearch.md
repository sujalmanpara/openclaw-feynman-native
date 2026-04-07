# Autoresearch

Use this workflow for autonomous iterative experiment loops that try ideas, measure results, keep what works, and discard what doesn't.

## Trigger phrases
- optimize this metric
- run an experiment loop
- improve performance iteratively
- automate benchmarking
- try ideas and keep what works

## Deliverable
- Plan: `outputs/.plans/<slug>.md`
- Final summary: `outputs/<slug>.md`
- Experiment code and logs: `experiments/<slug>/`
- Provenance sidecar: `outputs/<slug>.provenance.md`

## Execution contract

### 1. Gather requirements
Before doing anything, collect from the user:
- what to optimize (metric name, unit, direction: lower/higher is better)
- the benchmark command to run
- files in scope for changes
- maximum number of iterations (default: 20)

### 2. Confirm execution environment
Ask the user before running:

| Option | Description |
|---|---|
| **Local** | run in the current directory |
| **New git branch** | create a branch so main stays clean |
| **Virtual env** | create an isolated venv/conda first |
| **Docker** | run inside a container |
| **Plan only** | produce the plan without executing |

Do not start the loop without explicit confirmation.

### 3. Present the full plan
```
Optimization target: [metric] ([direction])
Benchmark command:   [command]
Files in scope:      [files]
Environment:         [chosen environment]
Max iterations:      [N]
```

Get user confirmation.

### 4. Run the loop
Each iteration:
1. propose a change
2. implement it
3. run the benchmark
4. record the result
5. keep or revert based on the metric
6. repeat

Track every iteration in a log file under `experiments/<slug>/`:
```md
| Iteration | Change | Result | Kept |
|---|---|---|---|
| 0 | baseline | [value] | — |
| 1 | [description] | [value] | yes/no |
```

### 5. Stop conditions
- user interrupts
- max iterations reached
- a blocking failure occurs
- metric converges (no improvement for N consecutive iterations)

### 6. Report
Write the final summary to `outputs/<slug>.md` with:
- optimization target and baseline
- best result achieved
- iteration log summary
- what worked and what didn't
- open questions

### 7. Provenance
Generate provenance sidecar.

## Minimum acceptance bar
- plan confirmed before execution
- every iteration logged
- honest metric tracking
- final summary with baseline vs best comparison
