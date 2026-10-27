[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [AI video](../README.md#ai) / ComfyUI-WanVideoWrapper

# ComfyUI-WanVideoWrapper

Community Wan nodes for ComfyUI

| Fact | Recorded value |
| --- | --- |
| License | Apache-2.0 |
| Stars | 6.7k |
| Last push | 2026-05-24 |
| Stack | Python |

## Overview

Community Wan nodes for ComfyUI — Python. Last push May 2026.

## Install

This is a ComfyUI custom-node pack. Install ComfyUI first. The README’s author also writes that native Wan support in ComfyUI should be preferred unless you need a feature that is not upstream yet.

```
git clone https://github.com/kijai/ComfyUI-WanVideoWrapper custom_nodes/ComfyUI-WanVideoWrapper
pip install -r custom_nodes/ComfyUI-WanVideoWrapper/requirements.txt
```

Portable Windows, from the README, run inside the portable folder:

```
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-WanVideoWrapper\requirements.txt
```

The README’s step 1 is “clone this repo into `custom_nodes`”; the clone command above is that step with the repository URL. Model files are listed on Hugging Face, not installed by pip.

> **Check this.** Dependency commands from the ComfyUI-WanVideoWrapper README, checked 26 Oct 2026.

## Quick start

Restart ComfyUI and add the wrapper’s Wan nodes. The README points at [Kijai/WanVideo_comfy](https://huggingface.co/Kijai/WanVideo_comfy/tree/main) and an fp8 scaled set for weights.

## Caveats

> Last push May 2026

## Links

- [GitHub](https://github.com/kijai/ComfyUI-WanVideoWrapper)
- [README](https://github.com/kijai/ComfyUI-WanVideoWrapper#installation)
- [Models](https://huggingface.co/Kijai/WanVideo_comfy/tree/main)
