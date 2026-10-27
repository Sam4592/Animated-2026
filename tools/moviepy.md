[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [Pipeline & CLI](../README.md#pipeline) / MoviePy

# MoviePy

Scripted cutting, compositing, captions and titles

| Fact | Recorded value |
| --- | --- |
| License | MIT |
| Stars | 15.0k |
| Last push | 2026-08-26 |
| Stack | Python |

## Overview

Scripted cutting, compositing, captions and titles — Python. An editing library, not an animation engine.

## Install

The README says MoviePy runs on Windows, Mac, and Linux with Python 3.9+, and that v2.0 has breaking changes from v1.

```
pip install moviepy
```

For a custom FFmpeg build or preview extras, the README points at the [install section](https://zulko.github.io/moviepy/getting_started/install.html) of the docs. Development install: `pip install -e .` from a clone.

> **Check this.** Command from the MoviePy README, checked 26 Oct 2026. The README spells the sentence “Intall moviepy”; the command itself is `pip install moviepy`.

## Quick start

The README’s example imports `VideoFileClip`, `TextClip`, and `CompositeVideoClip`, trims with `.subclipped()`, and writes with `.write_videofile("result.mp4")`.

## Caveats

> An editing library, not an animation engine

## Links

- [GitHub](https://github.com/Zulko/moviepy)
- [Docs](https://zulko.github.io/moviepy/)
- [Install](https://zulko.github.io/moviepy/getting_started/install.html)
