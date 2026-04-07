# RunPod Compute Adapter

Use RunPod for persistent GPU pods with SSH access when the user needs long-running experiments, large datasets, or multi-step work.

## Prerequisites
- `runpodctl` CLI installed
- API key configured: `runpodctl config --apiKey=YOUR_KEY`
- check availability: `command -v runpodctl`
- if not available, fall back to local/Docker/Modal execution and inform the user

## Commands

| Command | Description |
|---|---|
| `runpodctl create pod --gpuType "NVIDIA A100 80GB PCIe" --imageName "runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04" --name <slug>` | create a pod |
| `runpodctl get pod` | list all pods |
| `runpodctl stop pod <id>` | stop (preserves volume) |
| `runpodctl start pod <id>` | resume a stopped pod |
| `runpodctl remove pod <id>` | terminate and delete |
| `runpodctl gpu list` | list available GPU types and prices |
| `runpodctl send <file>` | transfer files to pods |
| `runpodctl receive <code>` | receive transferred files |

## SSH access
```bash
ssh root@<IP> -p <PORT> -i ~/.ssh/id_ed25519
```
Get connection details from `runpodctl get pod <id>`.

## GPU types
`NVIDIA GeForce RTX 4090`, `NVIDIA RTX A6000`, `NVIDIA A40`, `NVIDIA A100 80GB PCIe`, `NVIDIA H100 80GB HBM3`

## When to use
- long-running experiments needing persistent state
- large dataset processing
- multi-step work with SSH between iterations
- best for replication workflows that take hours

## Rules
- always stop or remove pods after experiments complete
- always confirm environment with the user before provisioning
- track pod lifecycle in the experiment log
