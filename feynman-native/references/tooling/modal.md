# Modal Compute Adapter

Use Modal for serverless GPU workloads when the user needs remote compute for training, inference, benchmarks, or batch processing.

## Prerequisites
- `pip install modal && modal setup`
- check availability: `command -v modal`
- if not available, fall back to local/Docker execution and inform the user

## Commands

| Command | Description |
|---|---|
| `modal run script.py` | run a script on Modal (ephemeral) |
| `modal run --detach script.py` | run detached (background) |
| `modal deploy script.py` | deploy persistently |
| `modal shell --gpu a100` | interactive shell with GPU |
| `modal app list` | list deployed apps |

## GPU types
`T4`, `L4`, `A10G`, `L40S`, `A100`, `A100-80GB`, `H100`, `H200`, `B200`

Multi-GPU: `"H100:4"` for 4x H100s.

## Script pattern
```python
import modal

app = modal.App("experiment")
image = modal.Image.debian_slim(python_version="3.11").pip_install("torch==2.8.0")

@app.function(gpu="A100", image=image, timeout=600)
def train():
    import torch
    # training code here

@app.local_entrypoint()
def main():
    train.remote()
```

## When to use
- stateless burst GPU jobs
- no persistent state needed between runs
- best for replication and autoresearch workflows that need GPU compute

## Integration with workflows
- replication: write a Modal-decorated script, execute with `modal run`
- autoresearch: run each iteration's benchmark via `modal run`
- the workflow should save results locally after each Modal run
