[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / LTX-Video

# LTX-Video

Earlier, permissively licensed LTX model

| Fact | Recorded value |
| --- | --- |
| License | Apache-2.0 |
| Stars | 11.2k |
| Last push | 2026-01-05 |
| Stack | Python |

## Overview

Earlier, permissively licensed LTX model — Python. Superseded by LTX-2.

## Install

The README says this codebase was tested with Python 3.10.5 and CUDA 12.2, and supports PyTorch >= 2.1.2. On macOS, MPS was tested with PyTorch 2.3.0 and should support PyTorch == 2.3 or >= 2.6.

```
git clone https://github.com/Lightricks/LTX-Video.git
cd LTX-Video
python -m venv env
source env/bin/activate
python -m pip install -e .[inference]
```

On some shells the extras bracket must be quoted: `pip install -e ".[inference]"`. The README writes it as `.\[inference]` inside a bash fence. Optional FP8 kernels are a separate repository, for Ada and later.

> **Check this.** Steps from the LTX-Video README, checked 26 Oct 2026. The README says LTX-2 has replaced this line of models.

## Quick start

The README recommends the ComfyUI workflow for quality. The local script it shows:

```
python inference.py --prompt "PROMPT" --conditioning_media_paths IMAGE_PATH --conditioning_start_frames 0 --height HEIGHT --width WIDTH --num_frames NUM_FRAMES --seed SEED --pipeline_config configs/ltxv-13b-0.9.8-distilled.yaml
```

## Caveats

> Superseded by LTX-2

## Links

- [GitHub](https://github.com/Lightricks/LTX-Video)
- [README](https://github.com/Lightricks/LTX-Video#quick-start-guide)
- [Diffusers](https://huggingface.co/docs/diffusers/main/en/api/pipelines/ltx_video)
- [ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo/)
