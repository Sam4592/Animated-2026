[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / LTX-2

# LTX-2

Video generation with synchronized audio (LTX-2.5 weights, v1.5.0)

| Fact | Recorded value |
| --- | --- |
| License | LTX-2.x Community License |
| Stars | 9.9k |
| Last push | 2026-10-18 |
| Stack | Python |

## Overview

Video generation with synchronized audio (LTX-2.5 weights, v1.5.0) — Python. Entities with $10M+ annual revenue need a paid license.

## Install

The README quick start uses `uv`. The `natten` extra is the fastest video-VAE backend and is Linux + CUDA only; on Windows and macOS it is skipped. The distilled LTX-2.5 download is about 66 GiB. Hugging Face may require you to accept the model terms and log in.

```
git clone https://github.com/Lightricks/LTX-2.git
cd LTX-2
uv sync --extra natten
hf auth login
hf download Lightricks/LTX-2.5 \
    diffusion_models/ltx-2.5-22b-distilled-transformer-bf16.safetensors \
    text_encoders/gemma4-12b-with-proj-ltx-2.5-bf16.safetensors \
    vae/ltx-2.5-video-vae-bf16.safetensors \
    vae/ltx-2.5-audio-vae-bf16.safetensors \
    latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors \
    --local-dir models/ltx-2.5
```

Low memory, from the README: add `--quantization fp8-cast --offload {cpu, disk}`. The README does not print a single minimum VRAM number in the quick start.

> **Check this.** Commands from the LTX-2 README, checked 26 Oct 2026.

## Quick start

Fast path is `uv run python -m ltx_pipelines.distilled` with the five checkpoint paths from the download. The README’s example `--prompt` is a long paragraph; copy it from the Quick Start rather than a shortened stand-in. Production quality is `uv run python -m ltx_pipelines.dfr_pipeline` after an extra LoRA download, and it uses more VRAM.

> **Check this.** Commercial entities with $10M+ annual revenue need a paid license. See [Licenses](../licenses.md).

## Caveats

> Entities with $10M+ annual revenue need a paid license

## Links

- [GitHub](https://github.com/Lightricks/LTX-2)
- [README](https://github.com/Lightricks/LTX-2#quick-start)
- [Weights](https://huggingface.co/Lightricks/LTX-2.5)
- [License](https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x)
- [ComfyUI](https://github.com/Lightricks/ComfyUI-LTXVideo/)
