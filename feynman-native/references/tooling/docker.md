# Docker Execution Environment

Use Docker when the user selects it as the execution environment for replication, autoresearch, or any experiment that benefits from isolation.

## When to use
- user selects "Docker" as the execution environment
- running untrusted code from a paper's repository
- experiments that install packages or modify system state
- any time the user asks to run something "safely" or "isolated"

## Prerequisites
- Docker must be installed and running locally
- check: `command -v docker && docker info >/dev/null 2>&1`
- if Docker is not available, fall back to local or virtualenv execution and inform the user

## Base image selection

| Research type | Base image |
|---|---|
| Python ML/DL | `pytorch/pytorch:latest` or `tensorflow/tensorflow:latest-gpu` |
| Python general | `python:3.11` |
| Node.js | `node:20` |
| R / statistics | `rocker/r-ver:4` |
| Julia | `julia:1.10` |
| Multi-language | `ubuntu:24.04` with manual installs |

## Execution patterns

### One-shot experiment
```bash
docker run --rm -v "$(pwd)":/workspace -w /workspace python:3.11 bash -c "
  pip install -r requirements.txt &&
  python train.py
"
```

### With GPU
```bash
docker run --rm --gpus all -v "$(pwd)":/workspace -w /workspace pytorch/pytorch:latest bash -c "
  pip install -r requirements.txt &&
  python train.py
"
```
Requires NVIDIA Container Toolkit.

### From project Dockerfile
```bash
docker build -t feynman-experiment .
docker run --rm -v "$(pwd)/results":/workspace/results feynman-experiment
```

### Persistent container for iterative work
For autoresearch loops, create a named container:
```bash
docker create --name <slug>-exp -v "$(pwd)":/workspace -w /workspace python:3.11 tail -f /dev/null
docker start <slug>-exp
docker exec <slug>-exp bash -c "pip install -r requirements.txt"
docker exec <slug>-exp bash -c "python train.py"
```

Clean up after:
```bash
docker stop <slug>-exp && docker rm <slug>-exp
```

## Rules
- mounted workspace syncs results back to the host automatically
- containers are network-enabled by default — add `--network none` for full isolation
- always confirm environment with the user before running
- always clean up containers after experiments complete
