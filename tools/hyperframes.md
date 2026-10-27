[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)

[Catalog](../README.md) / [Code-driven](../README.md#code) / HyperFrames

# HyperFrames

HTML/CSS + seekable animations to deterministic MP4; built for AI coding agents

| Fact | Recorded value |
| --- | --- |
| License | Apache-2.0 |
| Stars | 72.9k |
| Last push | 2026-10-26 |
| Stack | TypeScript, HTML/CSS, Node 22+ |

## Overview

HTML/CSS + seekable animations to deterministic MP4; built for AI coding agents — TypeScript, HTML/CSS, Node 22+. Pre-1.0 (v0.8.206 shipped today), so expect API churn.

## Install

The README’s manual path is the CLI. It requires **Node.js 22+** and **FFmpeg**.

```
npx hyperframes init my-video
cd my-video
```

For an AI coding agent, the same README also documents `npx hyperframes skills update`, or the Claude Code plugin commands below.

```
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

> **Check this.** Commands and the Node.js 22+ / FFmpeg requirement are from the HyperFrames README, checked 26 Oct 2026.

## Quick start

```
npx hyperframes preview
npx hyperframes render
```

`preview` opens a browser preview. `render` writes an MP4. Full walkthrough: [hyperframes.heygen.com/quickstart](https://hyperframes.heygen.com/quickstart).

## Caveats

> Pre-1.0 (v0.8.206 shipped today), so expect API churn

## Links

- [GitHub](https://github.com/heygen-com/hyperframes)
- [Docs](https://hyperframes.heygen.com/introduction)
- [Quickstart](https://hyperframes.heygen.com/quickstart)
- [npm](https://www.npmjs.com/package/hyperframes)
