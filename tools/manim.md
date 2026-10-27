[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [Pipeline & CLI](../README.md#pipeline) / Manim (Community)

# Manim (Community)

Math and technical explainer animations (v0.22.0, 8 Oct 2026)

| Fact | Recorded value |
| --- | --- |
| License | MIT |
| Stars | 41.9k |
| Last push | 2026-10-26 |
| Stack | Python |

## Overview

Math and technical explainer animations (v0.22.0, 8 Oct 2026) — Python. Needs FFmpeg and, for formulas, LaTeX installed.

## Install

The README does not paste commands. It says to follow the docs, and warns these steps are for the community edition only. The installation page says that if a Python environment already exists:

```
pip install manim
```

The local guide (docs for v0.22.0) recommends [uv](https://docs.astral.sh/uv/#getting-started), then:

```
uv python install
uv init manimations
cd manimations
uv add manim
uv run manim checkhealth
```

Before `uv add`, that guide says macOS needs `brew install cairo pkg-config`. Debian-based Linux:

```
sudo apt update
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev
```

LaTeX is optional and required for typeset formulas. The guide’s examples include MiKTeX on Windows, MacTeX on macOS, and `sudo apt install texlive-full` on Debian. A community Docker image is `manimcommunity/manim`.

> **Check this.** Commands from docs.manim.community installation pages linked by the README, checked 26 Oct 2026.

## Quick start

Save a scene as `example.py` and, from the README:

```
manim -p -ql example.py SquareToCircle
```

With uv, run it as `uv run manim -p -ql example.py SquareToCircle`. `-p` previews and `-ql` is low quality.

## Caveats

> Needs FFmpeg and, for formulas, LaTeX installed

## Links

- [GitHub](https://github.com/ManimCommunity/manim)
- [Installation](https://docs.manim.community/en/stable/installation.html)
- [Local install (uv)](https://docs.manim.community/en/stable/installation/uv.html)
- [Docker](https://docs.manim.community/en/stable/installation/docker.html)
