[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / Wan 2.2

# Wan 2.2

Text/image-to-video, Wan2.2-Animate character animation, speech-to-video

| Fact | Recorded value |
| --- | --- |
| License | Apache-2.0 |
| Stars | 18.2k |
| Last push | 2026-09-21 |
| Stack | Python |

## Overview

Text/image-to-video, Wan2.2-Animate character animation, speech-to-video — Python. 14B models need large GPUs; the 5B TI2V model targets a 4090-class card.

## Install

The README says `torch >= 2.4.0`. If `flash_attn` fails, install the other packages first.

```
git clone https://github.com/Wan-Video/Wan2.2.git
cd Wan2.2
pip install -r requirements.txt
```

Speech-to-video with CosyVoice also needs `pip install -r requirements_s2v.txt`. Download one checkpoint, for example the 5B model:

```
pip install "huggingface_hub[cli]"
huggingface-cli download Wan-AI/Wan2.2-TI2V-5B --local-dir ./Wan2.2-TI2V-5B
```

GPU notes written in the README: the single-GPU 14B text-to-video command needs at least 80 GB VRAM. The TI2V-5B command below can run on a GPU with at least 24 GB VRAM, and the README gives an RTX 4090 as the example. The 5B model is described as runnable on consumer cards such as a 4090.

> **Check this.** Commands and VRAM notes from the Wan2.2 README, checked 26 Oct 2026.

## Quick start

```
python generate.py --task ti2v-5B --size 1280*704 --ckpt_dir ./Wan2.2-TI2V-5B --offload_model True --convert_model_dtype --t5_cpu --prompt "Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage"
```

## Caveats

> 14B models need large GPUs; the 5B TI2V model targets a 4090-class card

## Links

- [GitHub](https://github.com/Wan-Video/Wan2.2)
- [README](https://github.com/Wan-Video/Wan2.2#run-wan22)
- [TI2V-5B weights](https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B)
