[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / ToonCrafter

# ToonCrafter

Generating in-between frames for cartoons

| Fact | Recorded value |
| --- | --- |
| License | Apache-2.0 |
| Stars | 6.0k |
| Last push | 2025-03-19 |
| Stack | Python |

## Overview

Generating in-between frames for cartoons — Python. Research code; no pushes since Mar 2025.

## Install

The README recommends Anaconda and pins Python 3.8.5. It does not print a `git clone` line; clone the repository, then:

```
git clone https://github.com/Doubiiu/ToonCrafter.git
cd ToonCrafter
conda create -n tooncrafter python=3.8.5
conda activate tooncrafter
pip install -r requirements.txt
```

Download `model.ckpt` from the Hugging Face link in the README and place it at `checkpoints/tooncrafter_512_interp_v1/model.ckpt`. The model card in the README lists about 24 GB GPU memory on an A100 for the 512 model (about 24–27 GB in this implementation; a community build lowered that toward 10 GB).

> **Check this.** Environment commands and memory note from the ToonCrafter README, checked 26 Oct 2026. The clone line adds the repository URL the README assumes you already have.

## Quick start

```
sh scripts/run.sh
```

Or `python gradio_app.py` after the checkpoint is in place. The README says clips are up to 16 frames at 512×320.

## Caveats

> Research code; no pushes since Mar 2025

## Links

- [GitHub](https://github.com/Doubiiu/ToonCrafter)
- [README](https://github.com/Doubiiu/ToonCrafter#setup)
- [Weights](https://huggingface.co/Doubiiu/ToonCrafter/blob/main/model.ckpt)
