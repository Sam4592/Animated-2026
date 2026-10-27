[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / LivePortrait

# LivePortrait

Animating a still portrait from a driving video

| Fact | Recorded value |
| --- | --- |
| License | MIT (code) |
| Stars | 19.3k |
| Last push | 2026-06-01 |
| Stack | Python |

## Overview

Animating a still portrait from a driving video — Python. Repo moved to KlingAIResearch; check bundled model licenses.

## Install

The README requires git, conda, and FFmpeg. It still tells you to clone `KlingTeam/LivePortrait`. This catalog’s GitHub link is `KlingAIResearch/LivePortrait`, which is where the repository lives after the move noted in the research.

```
git clone https://github.com/KlingTeam/LivePortrait
cd LivePortrait
conda create -n LivePortrait python=3.10
conda activate LivePortrait
pip install -r requirements.txt
```

Linux and Windows: the README shows example PyTorch installs for CUDA 11.1, 11.8, and 12.1, and says to match `nvcc -V`. Animals mode needs X-Pose; humans mode can skip that CUDA check. macOS Apple Silicon uses `pip install -r requirements_macOS.txt` and does not support animals mode. Intel macOS is not tested.

Weights:

```
huggingface-cli download KlingTeam/LivePortrait --local-dir pretrained_weights --exclude "*.git*" "README.md" "docs"
```

> **Check this.** Commands from the LivePortrait README on KlingAIResearch/LivePortrait, checked 26 Oct 2026. Model files may have their own licenses.

## Quick start

```
python inference.py
```

On Apple Silicon the README uses `PYTORCH_ENABLE_MPS_FALLBACK=1 python inference.py` and says it may be about 20× slower than an RTX 4090. A successful run writes `animations/s6--d0_concat.mp4`.

## Caveats

> Repo moved to KlingAIResearch; check bundled model licenses

## Links

- [GitHub](https://github.com/KlingAIResearch/LivePortrait)
- [README](https://github.com/KlingAIResearch/LivePortrait#getting-started-)
