[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [Pipeline & CLI](../README.md#pipeline) / ManimGL (3b1b)

# ManimGL (3b1b)

3Blue1Brown's own engine with interactive preview

| Fact | Recorded value |
| --- | --- |
| License | MIT |
| Stars | 95.7k |
| Last push | 2026-09-09 |
| Stack | Python, OpenGL |

## Overview

3Blue1Brown's own engine with interactive preview — Python, OpenGL. Different API from Community Manim; thinner docs.

## Install

The package name is `manimgl`, not `manim`. Python 3.10 or higher. System requirements named in the README: FFmpeg, OpenGL, and optional LaTeX. Linux also needs Pango development headers.

### pip

```
pip install manimgl
manimgl
```

### Ubuntu / Debian, from the README

```
sudo apt update
sudo apt install ffmpeg python3-pip libpango1.0-dev
sudo apt install texlive-science texlive-fonts-extra texlive-latex-extra
git clone https://github.com/3b1b/manim.git
cd manim
python3 -m pip install -e .
manimgl example_scenes.py OpeningManimExample
```

### macOS, from the README

```
brew install ffmpeg mactex
git clone https://github.com/3b1b/manim.git
cd manim
pip install -e .
manimgl example_scenes.py OpeningManimExample
```

On Apple silicon the README also says `arch -arm64 brew install pkg-config cairo`. It notes MacTeX is large and points at BasicTeX as a smaller option. Windows steps in the README: install FFmpeg, install MiKTeX, then the same clone and `pip install -e .`.

> **Check this.** Commands from the 3b1b/manim README, checked 26 Oct 2026. Do not use these commands to install Manim Community.

## Quick start

```
manimgl example_scenes.py OpeningManimExample
```

## Caveats

> Different API from Community Manim; thinner docs

## Links

- [GitHub](https://github.com/3b1b/manim)
- [Docs](https://3b1b.github.io/manim/)
