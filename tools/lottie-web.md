[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [Lottie & vector](../README.md#lottie) / lottie-web

# lottie-web

Playing After Effects-exported Lottie animations

| Fact | Recorded value |
| --- | --- |
| License | MIT |
| Stars | 32.3k |
| Last push | 2025-09-01 |
| Stack | JavaScript |

## Overview

Playing After Effects-exported Lottie animations — JavaScript. No video export; render frames through a code-driven pipeline.

## Install

For playback in a web page, the README’s HTML player install is:

```
npm install lottie-web
```

It also mentions `bower install bodymovin` and a cdnjs build. The After Effects exporter (Bodymovin) is a separate plugin; the README’s preferred install is the aescripts listing, with a Homebrew cask path `brew tap danielbayley/adobe` then `brew cask install lottie`. That plugin is not required to play a JSON file you already have.

> **Check this.** npm command from the lottie-web README, checked 26 Oct 2026.

## Quick start

Include the player and load a JSON animation. The README’s usage section starts with `lottie.loadAnimation({...})`. There is no MP4 export in this library; to get a video file, render frames in another tool from this catalog.

## Caveats

> No video export; render frames through a code-driven pipeline

## Links

- [GitHub](https://github.com/airbnb/lottie-web)
- [Docs](https://airbnb.io/lottie/)
- [npm](https://www.npmjs.com/package/lottie-web)
