[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / ComfyUI

# ComfyUI

Node UI that runs Wan, LTX, Hunyuan and other video models (v0.42.1, 19 Oct 2026)

| Fact | Recorded value |
| --- | --- |
| License | GPL-3.0 |
| Stars | 143.2k |
| Last push | 2026-10-26 |
| Stack | Python |

## Overview

Node UI that runs Wan, LTX, Hunyuan and other video models (v0.42.1, 19 Oct 2026) — Python. Each model keeps its own license; needs a capable GPU.

## Install

The README recommends the [desktop app](https://www.comfy.org/download) for Windows and Mac. Portable Windows archives are also linked (Nvidia, AMD, Intel, and an older Nvidia CUDA 12.6 build for 10-series GPUs). The Nvidia portable build it describes ships Python 3.13 and PyTorch CUDA 13.0 and supports 20-series and newer.

### comfy-cli

```
pip install comfy-cli
comfy install
```

### Manual install

The README says to git clone the repo. Python 3.13 is “very well supported”; 3.14 works with possible custom-node issues. Nvidia PyTorch, then dependencies:

```
git clone https://github.com/Comfy-Org/ComfyUI.git
cd ComfyUI
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
pip install -r requirements.txt
python main.py
```

AMD, Intel, and Apple silicon commands are in the same Installing section (ROCm, XPU, and the Apple PyTorch nightly note). They are not copied in full here. A GPU is required for practical video models; the README also says each model has its own license.

> **Check this.** Commands from the ComfyUI README, checked 26 Oct 2026. The clone URL is the repository this catalog links.

## Quick start

The desktop app or `python main.py` opens the node graph in a browser. Put checkpoints in `models/checkpoints`. Video models such as Wan are separate downloads.

## Caveats

> Each model keeps its own license; needs a capable GPU

## Links

- [GitHub](https://github.com/Comfy-Org/ComfyUI)
- [Desktop download](https://www.comfy.org/download)
- [comfy-cli](https://docs.comfy.org/comfy-cli/getting-started)
- [Manual install](https://github.com/Comfy-Org/ComfyUI#manual-install-windows-linux)
