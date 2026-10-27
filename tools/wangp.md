[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / WanGP

# WanGP

Low-VRAM app for Wan, LTX, Hunyuan and more

| Fact | Recorded value |
| --- | --- |
| License | WanGP Community License 2.0 |
| Stars | 11.1k |
| Last push | 2026-10-25 |
| Stack | Python |

## Overview

Low-VRAM app for Wan, LTX, Hunyuan and more — Python. Free to use, but no reselling or paid hosting without a commercial license.

## Install

The README says some models run with as little as **6 GB of VRAM**, and that AMD RDNA 4, 3, 3.5, and 2 are supported. One-click scripts: `scripts/install.bat` or `scripts/install.sh`, then `scripts/run.bat` or `scripts/run.sh`.

Manual install for RTX 20-series through 50-series, as printed in the README. The clone URL in the README is `Wan2GP.git` (the GitHub repository is `WanGP`):

```
git clone https://github.com/deepbeepmeep/Wan2GP.git
cd Wan2GP
conda create -n wan2gp python=3.11.14
conda activate wan2gp
pip install torch==2.10.0 torchvision==0.25.0 torchaudio==2.10.0 --index-url https://download.pytorch.org/whl/cu130
pip install -r requirements.txt
```

GTX 10-series in the README uses Python 3.10.9 and a different PyTorch build:

```
pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/test/cu128
pip install -r requirements.txt
```

Windows Triton commands are a table in the README (3.6.x with PyTorch 2.10 on RTX 30–50, 3.2.x on RTX 20). AMD steps are in `docs/AMD-INSTALLATION.md`, not repeated here.

> **Check this.** Commands from the WanGP README, checked 26 Oct 2026.

## Quick start

```
python wgp.py
```

The README says the Guides tab lists recommended models on first launch, and that disabling browser GPU use can free VRAM.

## Caveats

> Free to use, but no reselling or paid hosting without a commercial license

## Links

- [GitHub](https://github.com/deepbeepmeep/WanGP)
- [Installation guide](https://github.com/deepbeepmeep/WanGP/blob/main/docs/INSTALLATION.md)
- [AMD](https://github.com/deepbeepmeep/WanGP/blob/main/docs/AMD-INSTALLATION.md)
- [Getting started](https://github.com/deepbeepmeep/WanGP/blob/main/docs/GETTING_STARTED.md)
- [License](https://github.com/deepbeepmeep/WanGP/blob/main/LICENSE.txt)
