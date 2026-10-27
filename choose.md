[Catalog](README.md) · [How to choose](choose.md) · [Licenses](licenses.md) · [Notes](notes.md)

[Home](README.md) / How to choose

*From the 26 Oct 2026 research notes*

# How to choose

Match the kind of picture to a path already in this catalog. The table is the short version. The list below is the same choice, by job.

**Code-driven, desktop apps, motion graphics, or AI video**

| You are making | Open | In this catalog |
| --- | --- | --- |
| A video described in code, HTML, or by an agent | [Code-driven](README.md#code) | [HyperFrames](tools/hyperframes.md) if you think in HTML/CSS. [Remotion](tools/remotion.md) if you are a React team and fine with its license. [Motion Canvas](tools/motion-canvas.md) or [Revideo](tools/revideo.md) for MIT. |
| Explainers, diagrams, math, encoding, or batch edits | [Pipeline & CLI](README.md#pipeline) | [Manim Community](tools/manim.md) for math. [FFmpeg](tools/ffmpeg.md) for encoding and batch jobs. [MoviePy](tools/moviepy.md) for scripted cutting, compositing, captions and titles. [editly](tools/editly.md) for a declarative JSON5 spec or CLI to a finished slideshow-style video. |
| Drawing, rigging, cel work, or a 3D scene | [2D/3D apps](README.md#apps) | [OpenToonz](tools/opentoonz.md) or [Tahoma2D](tools/tahoma2d.md) for production 2D. [Synfig](tools/synfig.md) for rigged vector. [Krita](tools/krita.md) or [Pencil2D](tools/pencil2d.md) for hand-drawn. [Blender](tools/blender.md) Grease Pencil for 2D in 3D. |
| Keyframed graphics, a node composite, or the final edit | [Motion graphics](README.md#motion) | [Friction](tools/friction.md) for After Effects-style vector work. [Natron](tools/natron.md) for node compositing. Blender’s compositor for 3D-heavy shots. [Kdenlive](tools/kdenlive.md) or [Shotcut](tools/shotcut.md) for editing. |
| Generated shots or character animation | [AI video](README.md#ai) | [ComfyUI](tools/comfyui.md) as the workbench with [Wan 2.2](tools/wan22.md) (Apache-2.0) first. [LTX-2](tools/ltx-2.md) when you need audio. [WanGP](tools/wangp.md) on low-VRAM GPUs. |
| Vector playback from an After Effects export | [Lottie & vector](README.md#lottie) | [lottie-web](tools/lottie-web.md) plays the exported JSON. No video export; render frames through a code-driven pipeline. |

## By job

1. **Videos from data, templates, or AI agents.** [HyperFrames](tools/hyperframes.md) if you think in HTML/CSS. [Remotion](tools/remotion.md) if you are a React team and fine with its license. [Motion Canvas](tools/motion-canvas.md) or [Revideo](tools/revideo.md) for MIT.
2. **Explainers, diagrams, and math.** [Manim Community](tools/manim.md). [Motion Canvas](tools/motion-canvas.md) for a visual timeline.
3. **Character or cel animation.** [OpenToonz](tools/opentoonz.md) or [Tahoma2D](tools/tahoma2d.md) for production 2D, [Synfig](tools/synfig.md) for rigged vector, [Krita](tools/krita.md) or [Pencil2D](tools/pencil2d.md) for hand-drawn, [Blender](tools/blender.md) Grease Pencil for 2D in 3D.
4. **Motion graphics and compositing.** [Friction](tools/friction.md) for After Effects-style vector work, [Natron](tools/natron.md) for node compositing, Blender’s compositor for 3D-heavy shots.
5. **AI-generated shots and animation.** [ComfyUI](tools/comfyui.md) as the workbench with [Wan 2.2](tools/wan22.md) (Apache-2.0) first. [LTX-2](tools/ltx-2.md) when you need audio. [WanGP](tools/wangp.md) on low-VRAM GPUs.
6. **Final assembly.** [Kdenlive](tools/kdenlive.md) or [Shotcut](tools/shotcut.md) for editing. [FFmpeg](tools/ffmpeg.md) underneath for encoding and batch jobs.

[Read the license gotchas](licenses.md) before you ship a product that embeds one of these tools.
