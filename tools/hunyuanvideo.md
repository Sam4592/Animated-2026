[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / HunyuanVideo 1.5

# HunyuanVideo 1.5

8.3B text/image-to-video; 14 GB minimum with offloading

| Fact | Recorded value |
| --- | --- |
| License | Tencent Hunyuan Community License |
| Stars | 4.6k |
| Last push | 2026-04-10 |
| Stack | Python |

## Overview

8.3B text/image-to-video; 14 GB minimum with offloading — Python. License does not apply in the EU, UK or South Korea.

## Install

README hardware: NVIDIA GPU with CUDA. Minimum GPU memory is **14 GB with model offloading**. More memory can turn offloading off. Software: **Linux**, Python 3.10 or higher, and a CUDA build that matches PyTorch. The README does not document Windows or macOS installs.

```
git clone https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5.git
cd HunyuanVideo-1.5
pip install -r requirements.txt
pip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python
```

Flash Attention, Flex-Block-Attention, SageAttention, and `sgl-kernel==0.3.18` are optional speedups with their own commands in the README. Download weights using `checkpoints-download.md` before generating.

> **Check this.** Requirements and commands from the HunyuanVideo-1.5 README, checked 26 Oct 2026.

## Quick start

Inference commands are in the README’s “Inference with Source Code” section and depend on which checkpoint you downloaded (480p text-to-video and image-to-video are linked from the model cards). This page does not copy a command that only works after a specific checkpoint layout.

> **Check this.** The Tencent Hunyuan Community License does not apply in the EU, the UK, or South Korea. See [Licenses](../licenses.md).

## Caveats

> License does not apply in the EU, UK or South Korea

## Links

- [GitHub](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5)
- [README](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5#dependencies-and-installation)
- [License](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE)
- [Checkpoints](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/checkpoints-download.md)
