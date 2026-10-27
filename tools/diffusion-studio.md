[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [Code-driven](../README.md#code) / Diffusion Studio Core

# Diffusion Studio Core

In-browser video compositing engine

| Fact | Recorded value |
| --- | --- |
| License | MPL-2.0 |
| Stars | 1.2k |
| Last push | 2025-11-18 |
| Stack | TypeScript, WebCodecs |

## Overview

In-browser video compositing engine — TypeScript, WebCodecs. No pushes since Nov 2025.

## Install

```
npm install @diffusionstudio/core
```

Recommended usage from the README:

```
import * as core from "@diffusionstudio/core";

const composition = new core.Composition();
```

The README says the page must send `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: credentialless` so SharedArrayBuffer works.

> **Check this.** The README says the engine is free if the rendered video keeps the “Made with Diffusion Studio” watermark. Removing the watermark requires a purchased license key. That is separate from the MPL-2.0 code license listed in this catalog.

> **Check this.** Install command, headers, and watermark note from the Diffusion Studio Core README, checked 26 Oct 2026.

## Quick start

The README’s examples load media with `core.Source.from` and compose clips in the browser. There is no CLI render command in the README’s getting-started section.

## Caveats

> No pushes since Nov 2025

## Links

- [GitHub](https://github.com/diffusionstudio/core)
- [Docs](https://docs.diffusion.studio/docs)
