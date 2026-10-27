[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / Open-Sora

# Open-Sora

Fully open model including training code (Open-Sora 2.0, 11B)

| Fact | Recorded value |
| --- | --- |
| License | Apache-2.0 |
| Stars | 29.9k |
| Last push | 2026-04-09 |
| Stack | Python |

## Overview

Fully open model including training code (Open-Sora 2.0, 11B) — Python. No new model since 2.0 in Mar 2025.

## Install

The README’s quickstart uses conda, Python 3.10, and PyTorch >= 2.4.0. `xformers` is pinned for CUDA 12.1 in the example; the comment says to match your CUDA version.

```
conda create -n opensora python=3.10
conda activate opensora
git clone https://github.com/hpcaitech/Open-Sora
cd Open-Sora
pip install -v .
pip install xformers==0.0.27.post2 --index-url https://download.pytorch.org/whl/cu121
pip install flash-attn --no-build-isolation
```

Weights:

```
pip install "huggingface_hub[cli]"
huggingface-cli download hpcai-tech/Open-Sora-v2 --local-dir ./ckpts
```

The README’s efficiency table is measured on H100/H800 GPUs. It does not state a minimum consumer-GPU size in the install section.

> **Check this.** Commands from the Open-Sora README, checked 26 Oct 2026.

## Quick start

One-GPU 256px text-to-video example from the README, with offloading:

```
torchrun --nproc_per_node 1 --standalone scripts/diffusion/inference.py configs/diffusion/inference/t2i2v_256px.py --save-dir samples --prompt "raining, sea" --offload True
```

## Caveats

> No new model since 2.0 in Mar 2025

## Links

- [GitHub](https://github.com/hpcaitech/Open-Sora)
- [README](https://github.com/hpcaitech/Open-Sora#quickstart)
- [Weights](https://huggingface.co/hpcai-tech/Open-Sora-v2)
