[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [Pipeline & CLI](../README.md#pipeline) / FFmpeg

# FFmpeg

The encoding/filters backbone under nearly every tool here

| Fact | Recorded value |
| --- | --- |
| License | LGPL-2.1+ (GPL with some options) |
| Stars | 65.8k |
| Last push | 2026-10-26 |
| Stack | C |

## Overview

The encoding/filters backbone under nearly every tool here — C. Enabling GPL components changes redistribution duties.

## Install

The GitHub README does not contain install commands. It says GitHub is not the review process and points at [ffmpeg.org](https://ffmpeg.org). The download page says FFmpeg only publishes source, and gives this clone of the official git server:

```
git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
```

That page links already-built packages rather than one project-owned installer:

- Linux: Debian and Ubuntu official packages, Fedora and RHEL via RPM Fusion, plus static builds at [BtbN/FFmpeg-Builds](https://github.com/BtbN/FFmpeg-Builds/releases).
- Windows: builds from [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) and [BtbN](https://github.com/BtbN/FFmpeg-Builds/releases).
- macOS: static builds at [evermeet.cx/ffmpeg](https://evermeet.cx/ffmpeg/).

> **Check this.** Clone command and package links from ffmpeg.org/download.html, checked 26 Oct 2026. This catalog does not add a brew or apt command the download page does not show.

## Quick start

After `ffmpeg` is on your `PATH`, the tool manual is [ffmpeg.org/ffmpeg.html](https://ffmpeg.org/ffmpeg.html). A version check is `ffmpeg -version`. The project’s own README does not include a sample encode command.

## Caveats

> Enabling GPL components changes redistribution duties

## Links

- [GitHub](https://github.com/FFmpeg/FFmpeg)
- [Website](https://ffmpeg.org/)
- [Download](https://ffmpeg.org/download.html)
- [ffmpeg tool](https://ffmpeg.org/ffmpeg.html)
