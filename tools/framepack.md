[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / FramePack

# FramePack

Practical image-to-video diffusion on consumer GPUs

| Fact | Recorded value |
| --- | --- |
| License | Apache-2.0 |
| Stars | 17.3k |
| Last push | 2025-10-16 |
| Stack | Python |

## Overview

Practical image-to-video diffusion on consumer GPUs — Python. No pushes since Oct 2025.

## Install

README requirements: Nvidia GPU in the RTX 30, 40, or 50 series with fp16 and bf16. GTX 10 and RTX 20 series are not tested. Linux or Windows. At least 6 GB of GPU memory. The README says a 60-second 30 fps clip with the 13B model can run in 6 GB.

### Windows

One-click package (CUDA 12.6 + PyTorch 2.6) linked from the README:

```
https://github.com/lllyasviel/FramePack/releases/download/windows/framepack_cu126_torch26.7z
```

Uncompress, run `update.bat`, then `run.bat`. The README says the first run downloads more than 30 GB of models.

### Linux

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt
python demo_gradio.py
```

The README recommends a separate Python 3.10. It says to try the default PyTorch attention before optional kernels such as `pip install sageattention==1.0.6`.

> **Check this.** Requirements and commands from the FramePack README, checked 26 Oct 2026.

## Quick start

The Gradio GUI is the quick start. The README documents `--share`, `--port`, and `--server` on `demo_gradio.py`.

## Caveats

> No pushes since Oct 2025

## Links

- [GitHub](https://github.com/lllyasviel/FramePack)
- [README](https://github.com/lllyasviel/FramePack#installation)
