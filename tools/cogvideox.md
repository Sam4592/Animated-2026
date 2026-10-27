[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / CogVideoX

# CogVideoX

Text/image-to-video research models

| Fact | Recorded value |
| --- | --- |
| License | Apache-2.0 (code) |
| Stars | 13.1k |
| Last push | 2025-11-04 |
| Stack | Python |

## Overview

Text/image-to-video research models — Python. Weights may carry their own license; check before commercial use.

## Install

The README says Python must be between 3.10 and 3.12 inclusive for both the SAT and Diffusers paths. Diffusers install shown there:

```
pip install -r requirements.txt
```

Then follow `inference/cli_demo.py`. SAT inference is a separate tree in `sat/README.md`; the README does not repeat those commands in the quick start.

GPU notes in the README: CogVideoX-2B can run on older GPUs such as a GTX 1080 Ti, and CogVideoX-5B on desktop GPUs such as an RTX 3060, if you follow `requirements.txt`. It also says the memory table was measured on NVIDIA A100 / H100 and that turning off CPU offload multiplies memory use. The README says the CogVideoX-2B weights were changed to Apache 2.0; other weights may differ.

> **Check this.** Install line and GPU notes from the CogVideo README, checked 26 Oct 2026. Clone first if you are not already in the repo: `git clone https://github.com/zai-org/CogVideo`.

## Quick start

The README treats prompt rewriting as part of getting a good result and points at `inference/convert_demo.py` before `inference/cli_demo.py`. There is no single one-line generate command in the quick-start section.

## Caveats

> Weights may carry their own license; check before commercial use

## Links

- [GitHub](https://github.com/zai-org/CogVideo)
- [README](https://github.com/zai-org/CogVideo#quick-start)
