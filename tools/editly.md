[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [Pipeline & CLI](../README.md#pipeline) / editly

# editly

Declarative JSON5 spec or CLI to a finished slideshow-style video

| Fact | Recorded value |
| --- | --- |
| License | MIT |
| Stars | 5.6k |
| Last push | 2025-05-12 |
| Stack | TypeScript, Node |

## Overview

Declarative JSON5 spec or CLI to a finished slideshow-style video — TypeScript, Node. No pushes since May 2025.

## Install

README requirements: Windows, macOS, or Linux; Node.js (latest LTS recommended, and v12.16.2 or newer on macOS); `ffmpeg` and `ffprobe` on `PATH`. Linux may need the system packages listed by [headless-gl](https://github.com/stackgl/headless-gl#system-dependencies). The package is ESM only.

```
npm i -g editly
```

> **Check this.** Command and requirements from the editly README, checked 26 Oct 2026.

## Quick start

```
editly --help
```

A one-line slideshow from the README (inputs are your own files):

```
editly \
  title:'My video' \
  clip1.mov \
  title:'THE END' \
  --fast \
  --audio-file-path /path/to/music.mp3
```

Or `editly my-spec.json5 --fast --out output.gif`.

## Caveats

> No pushes since May 2025

## Links

- [GitHub](https://github.com/mifi/editly)
- [README](https://github.com/mifi/editly#installing)
