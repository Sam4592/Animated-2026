[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / AnimateDiff

# AnimateDiff

Motion modules for Stable Diffusion image models

| Fact | Recorded value |
| --- | --- |
| License | Apache-2.0 |
| Stars | 12.3k |
| Last push | 2024-07-31 |
| Stack | Python |

## Overview

Motion modules for Stable Diffusion image models — Python. Stalled since Jul 2024; superseded by native video models.

## Install

The README also points at the Diffusers tutorial. For this repository:

```
git clone https://github.com/guoyww/AnimateDiff.git
cd AnimateDiff
pip install -r requirements.txt
```

The README says checkpoints download automatically the first time a script runs. It does not state a GPU size or CUDA version in the quick start.

> **Check this.** Commands from the AnimateDiff README, checked 26 Oct 2026.

## Quick start

```
python -m scripts.animate --config configs/prompts/1_animate/1_1_animate_RealisticVision.yaml
```

Samples are written to `samples/`.

## Caveats

> Stalled since Jul 2024; superseded by native video models

## Links

- [GitHub](https://github.com/guoyww/AnimateDiff)
- [README](https://github.com/guoyww/AnimateDiff#quick-start)
- [Diffusers](https://huggingface.co/docs/diffusers/api/pipelines/animatediff)
