#!/usr/bin/env python3
"""Generate the catalog as Markdown for browsing on GitHub, plus an HTML copy in docs/."""

from html import escape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
AS_OF = "26 Oct 2026"

CATEGORIES = [
    ("code", "Code-driven", "Code-driven", "Describe a video in code or HTML and render a file."),
    ("pipeline", "Pipeline & CLI", "Pipeline/CLI", "Script encoding, math explainers, and batch edits."),
    ("apps", "2D/3D apps", "2D/3D", "Desktop programs for drawing, rigging, and 3D."),
    ("motion", "Motion graphics", "Motion graphics", "Editors and compositors with keyframes or nodes."),
    ("ai", "AI video", "AI video", "Local models and node UIs that generate or animate footage."),
    ("lottie", "Lottie & vector", "Lottie", "Play vector animations exported from After Effects."),
]
CAT_NAME = {cid: name for cid, name, _nav, _blurb in CATEGORIES}
CAT_ANCHOR = {cid: cid for cid, *_ in CATEGORIES}


def e(value):
    return escape(str(value), quote=True)


def blocks(items):
    parts = []
    for kind, payload in items:
        if kind == "p":
            parts.append(f"<p>{payload}</p>")
        elif kind == "h3":
            parts.append(f"<h3>{e(payload)}</h3>")
        elif kind == "note":
            parts.append(f'<p class="callout"><strong>Check this.</strong> {payload}</p>')
        elif kind == "ul":
            lis = "".join(f"<li>{item}</li>" for item in payload)
            parts.append(f"<ul>{lis}</ul>")
        elif kind == "ol":
            lis = "".join(f"<li>{item}</li>" for item in payload)
            parts.append(f"<ol>{lis}</ol>")
        elif kind == "code":
            parts.append(f"<pre><code>{e(payload).rstrip()}</code></pre>")
        else:
            raise ValueError(kind)
    return "\n".join(parts)


def src(text):
    return ("note", text)


# Install and quick-start copy is taken from each project's README or the
# official docs that README points to, fetched 26 Oct 2026. Markup inside
# paragraphs is written as HTML on purpose.
TOOLS = [
    {
        "slug": "hyperframes",
        "name": "HyperFrames",
        "cat": "code",
        "url": "https://github.com/heygen-com/hyperframes",
        "license": "Apache-2.0",
        "stars": "72.9k",
        "pushed": "2026-10-26",
        "stack": "TypeScript, HTML/CSS, Node 22+",
        "best": "HTML/CSS + seekable animations to deterministic MP4; built for AI coding agents",
        "caveat": "Pre-1.0 (v0.8.206 shipped today), so expect API churn",
        "docs": [
            ("Docs", "https://hyperframes.heygen.com/introduction"),
            ("Quickstart", "https://hyperframes.heygen.com/quickstart"),
            ("npm", "https://www.npmjs.com/package/hyperframes"),
        ],
        "install": [
            ("p", "The README’s manual path is the CLI. It requires <strong>Node.js 22+</strong> and <strong>FFmpeg</strong>."),
            ("code", "npx hyperframes init my-video\ncd my-video"),
            ("p", "For an AI coding agent, the same README also documents <code>npx hyperframes skills update</code>, or the Claude Code plugin commands below."),
            ("code", "claude plugin marketplace add heygen-com/hyperframes\nclaude plugin install hyperframes@hyperframes"),
            src("Commands and the Node.js 22+ / FFmpeg requirement are from the HyperFrames README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("code", "npx hyperframes preview\nnpx hyperframes render"),
            ("p", "<code>preview</code> opens a browser preview. <code>render</code> writes an MP4. Full walkthrough: <a href=\"https://hyperframes.heygen.com/quickstart\">hyperframes.heygen.com/quickstart</a>."),
        ],
    },
    {
        "slug": "remotion",
        "name": "Remotion",
        "cat": "code",
        "url": "https://github.com/remotion-dev/remotion",
        "license": "Remotion License (source-available)",
        "stars": "67.9k",
        "pushed": "2026-10-26",
        "stack": "TypeScript, React",
        "best": "Templated, data-driven videos in React at scale (v4.0.539, 26 Oct 2026)",
        "caveat": "Paid company license for for-profit orgs over 3 people",
        "docs": [
            ("Docs", "https://www.remotion.dev/docs"),
            ("License", "https://github.com/remotion-dev/remotion/blob/main/LICENSE.md"),
            ("License page", "https://www.remotion.dev/license"),
        ],
        "install": [
            ("p", "The README says: if Node.js is already installed, run the scaffolder. Otherwise follow the <a href=\"https://www.remotion.dev/docs/\">installation page</a>."),
            ("code", "npx create-video@latest"),
            src("Command from the Remotion README, checked 26 Oct 2026. The README does not list a Node.js version number; it points at the docs for a full install."),
        ],
        "quick": [
            ("p", "The scaffolder asks how you want to start a React video project. Rendering options (Node.js, Lambda, client-side) are documented at <a href=\"https://www.remotion.dev/docs\">remotion.dev/docs</a>."),
            ("note", "Free for individuals, non-profits, and for-profits up to 3 employees. Larger companies need a company license. See <a href=\"../licenses.html\">Licenses</a>."),
        ],
    },
    {
        "slug": "motion-canvas",
        "name": "Motion Canvas",
        "cat": "code",
        "url": "https://github.com/motion-canvas/motion-canvas",
        "license": "MIT",
        "stars": "19.5k",
        "pushed": "2026-07-02",
        "stack": "TypeScript",
        "best": "Code-authored explainer animations with a live preview editor",
        "caveat": "Last tagged release v3.17.2 is from Dec 2024",
        "docs": [
            ("Quickstart", "https://motion-canvas.io/docs/quickstart"),
            ("Docs", "https://motion-canvas.io/docs"),
        ],
        "install": [
            ("p", "The repository README does not include install commands. It points at the <a href=\"https://motion-canvas.io/docs/quickstart\">getting started guide</a>, which says Node.js 16 or greater and then:"),
            ("code", "npm init @motion-canvas@latest"),
            ("p", "If that fails on an old npm, the same page gives <code>npm exec @motion-canvas/create@latest</code> (the bug it mentions was fixed in npm 8.15.1). After the prompts:"),
            ("code", "cd <project-path>\nnpm install\nnpm start"),
            src("Steps from motion-canvas.io/docs/quickstart, linked from the README and checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "The guide says the editor is at <code>http://localhost:9000/</code>. The scaffold can install an image-sequence exporter, a Video (FFmpeg) exporter, or both. The scene file it creates is <code>src/scenes/example.tsx</code>."),
        ],
    },
    {
        "slug": "revideo",
        "name": "Revideo",
        "cat": "code",
        "url": "https://github.com/midrender/revideo",
        "license": "MIT",
        "stars": "4.1k",
        "pushed": "2026-07-15",
        "stack": "TypeScript",
        "best": "Motion Canvas fork aimed at programmatic rendering and APIs",
        "caveat": "Repo moved from redotvideo to the midrender org; small community",
        "docs": [
            ("Docs", "https://docs.re.video/"),
            ("renderVideo", "https://docs.re.video/renderer/renderVideo/"),
        ],
        "install": [
            ("p", "The README’s getting started command:"),
            ("code", "npm init @revideo@latest"),
            ("p", "The README says headless rendering needs Node and a headless browser. It does not list a minimum Node version."),
            src("Command from the Revideo README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "A scene is a TypeScript generator passed to <code>makeScene2D</code>. Render with <a href=\"https://docs.re.video/renderer/renderVideo/\"><code>renderVideo()</code></a>. Telemetry can be turned off with <code>DISABLE_TELEMETRY=true</code>, as stated in the README."),
        ],
    },
    {
        "slug": "diffusion-studio",
        "name": "Diffusion Studio Core",
        "cat": "code",
        "url": "https://github.com/diffusionstudio/core",
        "license": "MPL-2.0",
        "stars": "1.2k",
        "pushed": "2025-11-18",
        "stack": "TypeScript, WebCodecs",
        "best": "In-browser video compositing engine",
        "caveat": "No pushes since Nov 2025",
        "docs": [("Docs", "https://docs.diffusion.studio/docs")],
        "install": [
            ("code", "npm install @diffusionstudio/core"),
            ("p", "Recommended usage from the README:"),
            ("code", 'import * as core from "@diffusionstudio/core";\n\nconst composition = new core.Composition();'),
            ("p", "The README says the page must send <code>Cross-Origin-Opener-Policy: same-origin</code> and <code>Cross-Origin-Embedder-Policy: credentialless</code> so SharedArrayBuffer works."),
            ("note", "The README says the engine is free if the rendered video keeps the “Made with Diffusion Studio” watermark. Removing the watermark requires a purchased license key. That is separate from the MPL-2.0 code license listed in this catalog."),
            src("Install command, headers, and watermark note from the Diffusion Studio Core README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "The README’s examples load media with <code>core.Source.from</code> and compose clips in the browser. There is no CLI render command in the README’s getting-started section."),
        ],
    },
    {
        "slug": "manimgl",
        "name": "ManimGL (3b1b)",
        "cat": "pipeline",
        "url": "https://github.com/3b1b/manim",
        "license": "MIT",
        "stars": "95.7k",
        "pushed": "2026-09-09",
        "stack": "Python, OpenGL",
        "best": "3Blue1Brown's own engine with interactive preview",
        "caveat": "Different API from Community Manim; thinner docs",
        "docs": [("Docs", "https://3b1b.github.io/manim/")],
        "install": [
            ("p", "The package name is <code>manimgl</code>, not <code>manim</code>. Python 3.10 or higher. System requirements named in the README: FFmpeg, OpenGL, and optional LaTeX. Linux also needs Pango development headers."),
            ("h3", "pip"),
            ("code", "pip install manimgl\nmanimgl"),
            ("h3", "Ubuntu / Debian, from the README"),
            ("code", "sudo apt update\nsudo apt install ffmpeg python3-pip libpango1.0-dev\nsudo apt install texlive-science texlive-fonts-extra texlive-latex-extra\ngit clone https://github.com/3b1b/manim.git\ncd manim\npython3 -m pip install -e .\nmanimgl example_scenes.py OpeningManimExample"),
            ("h3", "macOS, from the README"),
            ("code", "brew install ffmpeg mactex\ngit clone https://github.com/3b1b/manim.git\ncd manim\npip install -e .\nmanimgl example_scenes.py OpeningManimExample"),
            ("p", "On Apple silicon the README also says <code>arch -arm64 brew install pkg-config cairo</code>. It notes MacTeX is large and points at BasicTeX as a smaller option. Windows steps in the README: install FFmpeg, install MiKTeX, then the same clone and <code>pip install -e .</code>."),
            src("Commands from the 3b1b/manim README, checked 26 Oct 2026. Do not use these commands to install Manim Community."),
        ],
        "quick": [
            ("code", "manimgl example_scenes.py OpeningManimExample"),
        ],
    },
    {
        "slug": "ffmpeg",
        "name": "FFmpeg",
        "cat": "pipeline",
        "url": "https://github.com/FFmpeg/FFmpeg",
        "license": "LGPL-2.1+ (GPL with some options)",
        "stars": "65.8k",
        "pushed": "2026-10-26",
        "stack": "C",
        "best": "The encoding/filters backbone under nearly every tool here",
        "caveat": "Enabling GPL components changes redistribution duties",
        "docs": [
            ("Website", "https://ffmpeg.org/"),
            ("Download", "https://ffmpeg.org/download.html"),
            ("ffmpeg tool", "https://ffmpeg.org/ffmpeg.html"),
        ],
        "install": [
            ("p", "The GitHub README does not contain install commands. It says GitHub is not the review process and points at <a href=\"https://ffmpeg.org\">ffmpeg.org</a>. The download page says FFmpeg only publishes source, and gives this clone of the official git server:"),
            ("code", "git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg"),
            ("p", "That page links already-built packages rather than one project-owned installer:"),
            ("ul", [
                "Linux: Debian and Ubuntu official packages, Fedora and RHEL via RPM Fusion, plus static builds at <a href=\"https://github.com/BtbN/FFmpeg-Builds/releases\">BtbN/FFmpeg-Builds</a>.",
                "Windows: builds from <a href=\"https://www.gyan.dev/ffmpeg/builds/\">gyan.dev</a> and <a href=\"https://github.com/BtbN/FFmpeg-Builds/releases\">BtbN</a>.",
                "macOS: static builds at <a href=\"https://evermeet.cx/ffmpeg/\">evermeet.cx/ffmpeg</a>.",
            ]),
            src("Clone command and package links from ffmpeg.org/download.html, checked 26 Oct 2026. This catalog does not add a brew or apt command the download page does not show."),
        ],
        "quick": [
            ("p", "After <code>ffmpeg</code> is on your <code>PATH</code>, the tool manual is <a href=\"https://ffmpeg.org/ffmpeg.html\">ffmpeg.org/ffmpeg.html</a>. A version check is <code>ffmpeg -version</code>. The project’s own README does not include a sample encode command."),
        ],
    },
    {
        "slug": "manim",
        "name": "Manim (Community)",
        "cat": "pipeline",
        "url": "https://github.com/ManimCommunity/manim",
        "license": "MIT",
        "stars": "41.9k",
        "pushed": "2026-10-26",
        "stack": "Python",
        "best": "Math and technical explainer animations (v0.22.0, 8 Oct 2026)",
        "caveat": "Needs FFmpeg and, for formulas, LaTeX installed",
        "docs": [
            ("Installation", "https://docs.manim.community/en/stable/installation.html"),
            ("Local install (uv)", "https://docs.manim.community/en/stable/installation/uv.html"),
            ("Docker", "https://docs.manim.community/en/stable/installation/docker.html"),
        ],
        "install": [
            ("p", "The README does not paste commands. It says to follow the docs, and warns these steps are for the community edition only. The installation page says that if a Python environment already exists:"),
            ("code", "pip install manim"),
            ("p", "The local guide (docs for v0.22.0) recommends <a href=\"https://docs.astral.sh/uv/#getting-started\">uv</a>, then:"),
            ("code", "uv python install\nuv init manimations\ncd manimations\nuv add manim\nuv run manim checkhealth"),
            ("p", "Before <code>uv add</code>, that guide says macOS needs <code>brew install cairo pkg-config</code>. Debian-based Linux:"),
            ("code", "sudo apt update\nsudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev"),
            ("p", "LaTeX is optional and required for typeset formulas. The guide’s examples include MiKTeX on Windows, MacTeX on macOS, and <code>sudo apt install texlive-full</code> on Debian. A community Docker image is <code>manimcommunity/manim</code>."),
            src("Commands from docs.manim.community installation pages linked by the README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Save a scene as <code>example.py</code> and, from the README:"),
            ("code", "manim -p -ql example.py SquareToCircle"),
            ("p", "With uv, run it as <code>uv run manim -p -ql example.py SquareToCircle</code>. <code>-p</code> previews and <code>-ql</code> is low quality."),
        ],
    },
    {
        "slug": "moviepy",
        "name": "MoviePy",
        "cat": "pipeline",
        "url": "https://github.com/Zulko/moviepy",
        "license": "MIT",
        "stars": "15.0k",
        "pushed": "2026-08-26",
        "stack": "Python",
        "best": "Scripted cutting, compositing, captions and titles",
        "caveat": "An editing library, not an animation engine",
        "docs": [
            ("Docs", "https://zulko.github.io/moviepy/"),
            ("Install", "https://zulko.github.io/moviepy/getting_started/install.html"),
        ],
        "install": [
            ("p", "The README says MoviePy runs on Windows, Mac, and Linux with Python 3.9+, and that v2.0 has breaking changes from v1."),
            ("code", "pip install moviepy"),
            ("p", "For a custom FFmpeg build or preview extras, the README points at the <a href=\"https://zulko.github.io/moviepy/getting_started/install.html\">install section</a> of the docs. Development install: <code>pip install -e .</code> from a clone."),
            src("Command from the MoviePy README, checked 26 Oct 2026. The README spells the sentence “Intall moviepy”; the command itself is <code>pip install moviepy</code>."),
        ],
        "quick": [
            ("p", "The README’s example imports <code>VideoFileClip</code>, <code>TextClip</code>, and <code>CompositeVideoClip</code>, trims with <code>.subclipped()</code>, and writes with <code>.write_videofile(\"result.mp4\")</code>."),
        ],
    },
    {
        "slug": "editly",
        "name": "editly",
        "cat": "pipeline",
        "url": "https://github.com/mifi/editly",
        "license": "MIT",
        "stars": "5.6k",
        "pushed": "2025-05-12",
        "stack": "TypeScript, Node",
        "best": "Declarative JSON5 spec or CLI to a finished slideshow-style video",
        "caveat": "No pushes since May 2025",
        "docs": [("README", "https://github.com/mifi/editly#installing")],
        "install": [
            ("p", "README requirements: Windows, macOS, or Linux; Node.js (latest LTS recommended, and v12.16.2 or newer on macOS); <code>ffmpeg</code> and <code>ffprobe</code> on <code>PATH</code>. Linux may need the system packages listed by <a href=\"https://github.com/stackgl/headless-gl#system-dependencies\">headless-gl</a>. The package is ESM only."),
            ("code", "npm i -g editly"),
            src("Command and requirements from the editly README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("code", "editly --help"),
            ("p", "A one-line slideshow from the README (inputs are your own files):"),
            ("code", "editly \\\n  title:'My video' \\\n  clip1.mov \\\n  title:'THE END' \\\n  --fast \\\n  --audio-file-path /path/to/music.mp3"),
            ("p", "Or <code>editly my-spec.json5 --fast --out output.gif</code>."),
        ],
    },
    {
        "slug": "blender",
        "name": "Blender",
        "cat": "apps",
        "url": "https://github.com/blender/blender",
        "license": "GPL-2.0+",
        "stars": "21.3k",
        "pushed": "2026-10-26",
        "stack": "C++, Python",
        "best": "3D, Grease Pencil 2D, compositor and video editor in one (5.2.3 LTS, 22 Oct 2026)",
        "caveat": "GitHub is a mirror; development lives on projects.blender.org",
        "docs": [
            ("Download", "https://www.blender.org/download/"),
            ("Manual", "https://docs.blender.org/manual/en/latest/index.html"),
            ("Build", "https://developer.blender.org/docs/handbook/building_blender/"),
        ],
        "install": [
            ("p", "The GitHub README does not include an end-user install command. It links the <a href=\"https://www.blender.org\">main website</a> and says a clone of the GitHub mirror can hit Git LFS errors unless you set <code>GIT_LFS_SKIP_SMUDGE=1</code>."),
            ("p", "The official download page lists installers for Windows, Windows ARM, macOS Apple Silicon, Linux, Steam, and source. When checked on 26 Oct 2026 it showed <strong>v5.2.3 LTS</strong>, matching the version in this catalog."),
            ("p", "Building from source is documented at <a href=\"https://developer.blender.org/docs/handbook/building_blender/\">developer.blender.org</a>, not as the way to install the app."),
            src("Download options from blender.org/download, checked 26 Oct 2026. No package-manager command is printed on that page, so none is repeated here."),
        ],
        "quick": [
            ("p", "Install the build for your OS, then open Blender. Grease Pencil, the compositor, and the video sequence editor are part of the same application. The user manual is <a href=\"https://docs.blender.org/manual/en/latest/index.html\">docs.blender.org</a>."),
        ],
    },
    {
        "slug": "krita",
        "name": "Krita",
        "cat": "apps",
        "url": "https://github.com/KDE/krita",
        "license": "GPL-3.0",
        "stars": "10.6k",
        "pushed": "2026-10-26",
        "stack": "C++, Qt",
        "best": "Painted frame-by-frame animation",
        "caveat": "A painting app first; animation tools are basic",
        "docs": [
            ("Download", "https://krita.org/en/download/"),
            ("Manual", "https://docs.krita.org/en/user_manual.html"),
        ],
        "install": [
            ("p", "The GitHub README says this repository is a mirror of KDE Invent and points at <a href=\"https://www.krita.org\">krita.org</a>. It does not include a user install command."),
            ("p", "The download page, checked 26 Oct 2026, offers <strong>Krita 5.3.4.1</strong> (released Wednesday, 7 October 2026): a Windows installer, a macOS installer, and a Linux 64-bit AppImage, plus Steam and the Mac App Store."),
            src("Versions and installers from krita.org/en/download, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Animation is documented in the <a href=\"https://docs.krita.org/en/user_manual.html\">user manual</a>. The README’s nightly-build links are for testing, not the stable install."),
        ],
    },
    {
        "slug": "opentoonz",
        "name": "OpenToonz",
        "cat": "apps",
        "url": "https://github.com/opentoonz/opentoonz",
        "license": "BSD-3-Clause",
        "stars": "7.9k",
        "pushed": "2026-10-26",
        "stack": "C++",
        "best": "Production 2D cel and cut-out animation",
        "caveat": "Steep learning curve",
        "docs": [
            ("Download and requirements", "https://opentoonz.github.io/e/index.html"),
            ("Docs", "https://github.com/opentoonz/opentoonz_docs"),
            ("Releases", "https://github.com/opentoonz/opentoonz/releases"),
        ],
        "install": [
            ("p", "The README says to download the latest installer from <a href=\"https://opentoonz.github.io/e/index.html\">opentoonz.github.io</a>. Older and nightly builds are on the GitHub releases page. It does not publish a package-manager command."),
            ("p", "That site’s system requirements, checked 26 Oct 2026:"),
            ("ul", [
                "Windows: Windows 7 SP1, 8.1, or 10, 64-bit; Intel Core i series; 4 GB RAM or more; 500 MB free; 1280×1024 or higher.",
                "macOS: macOS 10.14 or later; Intel Core i series; 4 GB RAM or more; 500 MB free; 1280×1024 or higher.",
            ]),
            ("p", "The same page does not list a Linux requirement block. Linux build steps are in the repository’s <code>doc/how_to_build_linux.md</code>."),
            src("Installer location from the README; hardware list from opentoonz.github.io, both checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "General documentation is the separate <a href=\"https://github.com/opentoonz/opentoonz_docs\">opentoonz_docs</a> repository."),
        ],
    },
    {
        "slug": "synfig",
        "name": "Synfig Studio",
        "cat": "apps",
        "url": "https://github.com/synfig/synfig",
        "license": "GPL-3.0",
        "stars": "2.3k",
        "pushed": "2026-10-25",
        "stack": "C++",
        "best": "Vector tweening and bone rigging without frame-by-frame drawing",
        "caveat": "Latest tag v1.5.5 (Mar 2026) is on the development series",
        "docs": [
            ("Install guide", "https://synfig.readthedocs.io/en/latest/installation.html"),
            ("Stable download", "https://www.synfig.org/download-stable/"),
            ("Website", "https://synfig.org/"),
        ],
        "install": [
            ("p", "The README says Synfig Studio is available for Windows, Linux, and macOS, and links the <a href=\"https://synfig.readthedocs.io/en/latest/installation.html\">installation guide</a> instead of printing commands. That guide says:"),
            ("ul", [
                "Windows: download the .exe and run the wizard.",
                "Linux: download the AppImage, mark it executable, and double-click it.",
                "macOS: download the .dmg, drag Synfig Studio to Applications, and open it (the guide also covers the unidentified-developer prompt).",
            ]),
            ("p", "The stable download page is <a href=\"https://www.synfig.org/download-stable/\">synfig.org/download-stable</a>. Checked 26 Oct 2026, that page says Synfig is free under GPLv3 and that payment is optional. It did not show a direct installer URL in the page HTML, so this catalog does not invent one."),
            src("Steps from the installation guide linked by the README; download-page wording checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "After the app opens, the user manual’s next page is the <a href=\"https://synfig.readthedocs.io/en/latest/quick_start.html\">quick start</a>."),
        ],
    },
    {
        "slug": "pencil2d",
        "name": "Pencil2D",
        "cat": "apps",
        "url": "https://github.com/pencil2d/pencil",
        "license": "GPL-2.0",
        "stars": "1.8k",
        "pushed": "2026-10-26",
        "stack": "C++, Qt",
        "best": "Simple hand-drawn frame-by-frame",
        "caveat": "No rigging or tweening",
        "docs": [
            ("Download", "https://www.pencil2d.org/download/"),
            ("Releases", "https://github.com/pencil2d/pencil/releases"),
        ],
        "install": [
            ("p", "The README says to download from the <a href=\"https://www.pencil2d.org/download/\">official site</a> or GitHub releases. The download page, checked 26 Oct 2026, offers <strong>v0.7.2</strong> for Windows 7+, macOS 10.14+ (Intel and a separate mac build), and Linux AppImages. It also prints:"),
            ("code", "sudo pacman -S pencil2d\nsudo apt-get install pencil2d\nsudo dnf install Pencil2D\nflatpak install flathub org.pencil2d.Pencil2D\nbrew install --cask pencil2d"),
            ("p", "Those are alternative package routes on the same page (Arch, Debian/Ubuntu, Fedora, Flatpak, Homebrew). Use one, not all of them."),
            src("Links and commands from pencil2d.org/download, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Open the app and draw on frames. The project has no rigging or tweening tools, which is why the catalog lists that as the caveat."),
        ],
    },
    {
        "slug": "tahoma2d",
        "name": "Tahoma2D",
        "cat": "apps",
        "url": "https://github.com/tahoma2d/tahoma2d",
        "license": "BSD-3-Clause",
        "stars": "675",
        "pushed": "2026-10-17",
        "stack": "C++",
        "best": "OpenToonz-based 2D plus stop motion, friendlier defaults",
        "caveat": "Small team",
        "docs": [
            ("Download", "https://tahoma2d.org/download"),
            ("Releases", "https://github.com/tahoma2d/tahoma2d/releases"),
        ],
        "install": [
            ("p", "The README says requirements are on <a href=\"https://tahoma2d.org/download\">tahoma2d.org/download</a> and to download the latest release from GitHub. The download page has Windows, macOS, and Linux sections (official and nightly, portable and installer). The file URLs are filled in by page script, so this catalog does not copy a direct file link that was not in the HTML."),
            ("p", "Build notes are in the README’s “How to Build Locally” section, for people compiling rather than installing a release."),
            src("Install locations from the Tahoma2D README. The download page was fetched 26 Oct 2026; specific installer filenames were not in the static HTML."),
        ],
        "quick": [
            ("p", "Install a release build, then start Tahoma2D. It is an OpenToonz-based app with stop-motion features. There is no CLI quick start in the README."),
        ],
    },
    {
        "slug": "shotcut",
        "name": "Shotcut",
        "cat": "motion",
        "url": "https://github.com/mltframework/shotcut",
        "license": "GPL-3.0",
        "stars": "15.5k",
        "pushed": "2026-10-26",
        "stack": "C++, Qt, MLT",
        "best": "Cross-platform editing with keyframed filters",
        "caveat": "An editor, not an animation tool",
        "docs": [("Download", "https://www.shotcut.org/download/")],
        "install": [
            ("p", "The README says binaries are at <a href=\"https://www.shotcut.org/download/\">shotcut.org/download</a>. That page, checked 26 Oct 2026, lists version 26.9.27 builds for Windows 10/11 (Intel/AMD and ARM), macOS 12+, and Linux (portable tar and AppImage). Minimum Windows 10 build named there is 1809. Linux snap, from that page:"),
            ("code", "snap install shotcut --classic"),
            src("Snap command and OS list from shotcut.org/download, which the README links. Checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Open Shotcut and edit on the timeline. Keyframed filters are part of the editor. The README’s compile steps (<code>cmake</code>, then <code>cmake --install .</code>) are for building, not for a normal install."),
        ],
    },
    {
        "slug": "openshot",
        "name": "OpenShot",
        "cat": "motion",
        "url": "https://github.com/OpenShot/openshot-qt",
        "license": "GPL-3.0",
        "stars": "6.7k",
        "pushed": "2026-10-26",
        "stack": "Python, Qt",
        "best": "Beginner editing with keyframe animation",
        "caveat": "Basic keyframing only",
        "docs": [
            ("Download", "https://www.openshot.org/download/"),
            ("User guide", "https://www.openshot.org/user-guide/"),
        ],
        "install": [
            ("p", "The README says the quickest start is a pre-built installer from <a href=\"https://www.openshot.org/download/\">openshot.org/download</a>, and it mentions the Daily Builds section of that page."),
            ("p", "Checked 26 Oct 2026, the download page offers a Linux AppImage for v4.0.1 and this snap command:"),
            ("code", "sudo snap install openshot-qt"),
            ("p", "The same page has Windows and macOS tabs. Daily-build filenames change often, so they are not copied here."),
            src("Snap command from openshot.org/download. The README points at that page and at Daily Builds. Checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Launch OpenShot and use the timeline. Keyframe animation is basic, which is the caveat in this catalog. Tutorials are linked from the repository README."),
        ],
    },
    {
        "slug": "kdenlive",
        "name": "Kdenlive",
        "cat": "motion",
        "url": "https://github.com/KDE/kdenlive",
        "license": "GPL-3.0",
        "stars": "5.9k",
        "pushed": "2026-10-26",
        "stack": "C++, MLT",
        "best": "Assembling, keyframed effects, titles and final edit",
        "caveat": "An editor, not an animation tool",
        "docs": [("Download", "https://kdenlive.org/download/")],
        "install": [
            ("p", "The README does not include an install command. It says downloads for stable releases and daily builds are on <a href=\"https://kdenlive.org\">kdenlive.org</a>."),
            ("p", "The download page, checked 26 Oct 2026, lists <strong>26.08.2</strong>. The Windows standalone build says it requires Windows 10 or newer. Linux options on that page include an AppImage. macOS is a separate column on the same page. Daily builds are marked for testing."),
            src("Version and Windows 10 note from kdenlive.org/download, checked 26 Oct 2026. No single shell command is shown for every OS, so none is invented here."),
        ],
        "quick": [
            ("p", "Open Kdenlive, import clips, and use titles plus keyframed effects for the final edit. Developer build steps in the README are for contributors."),
        ],
    },
    {
        "slug": "natron",
        "name": "Natron",
        "cat": "motion",
        "url": "https://github.com/NatronGitHub/Natron",
        "license": "GPL-2.0",
        "stars": "5.6k",
        "pushed": "2026-07-24",
        "stack": "C++",
        "best": "Node-based compositing, After Effects/Nuke-like",
        "caveat": "Slow-moving development",
        "docs": [
            ("Download", "https://natrongithub.github.io/#download"),
            ("Releases", "https://github.com/NatronGitHub/Natron/releases"),
        ],
        "install": [
            ("p", "README requirements: GNU/Linux, macOS, or Windows, and a 32-bit x86 or 64-bit x86-64 CPU. Hardware-accelerated rendering wants OpenGL 2.0; otherwise software rendering is available (on Linux, <code>LIBGL_ALWAYS_SOFTWARE=1</code>)."),
            ("p", "Binaries for Linux, Windows, and macOS are on <a href=\"https://github.com/NatronGitHub/Natron/releases\">GitHub releases</a> and <a href=\"https://natrongithub.github.io/#download\">the website</a>. Linux Flatpak from the README:"),
            ("code", "flatpak install fr.natron.Natron"),
            src("Requirements and Flatpak command from the Natron README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Launch Natron and build a node graph. The README’s source-build files (<code>INSTALL_LINUX.md</code>, <code>INSTALL_MACOS.md</code>) are for compiling."),
        ],
    },
    {
        "slug": "friction",
        "name": "Friction",
        "cat": "motion",
        "url": "https://github.com/friction2d/friction",
        "license": "GPL-3.0",
        "stars": "1.9k",
        "pushed": "2026-10-16",
        "stack": "C++, Qt",
        "best": "After Effects-style vector motion graphics (enve fork)",
        "caveat": "Still a release candidate (v1.0.0-rc.3, 31 Dec 2025)",
        "docs": [
            ("Download", "https://friction.graphics/"),
            ("Documentation", "https://friction.graphics/documentation"),
        ],
        "install": [
            ("p", "The README links build instructions, not a binary install command. The project site’s download section, checked 26 Oct 2026, offers <strong>v1.0.0-rc.3</strong> for Windows (setup exe and a 7z), Linux (AppImage), and macOS (dmg), from the GitHub release assets. Example of the Windows setup linked there:"),
            ("code", "https://github.com/friction2d/friction/releases/download/v1.0.0-rc.3/friction-1.0.0-rc.3-setup-win64.exe"),
            ("p", "The same section links <code>Friction-1.0.0-rc.3-x86_64.AppImage</code> and <code>Friction-1.0.0-rc.3.dmg</code>. Snapshots are listed separately."),
            src("Release files from friction.graphics, checked 26 Oct 2026. The README itself only documents compiling."),
        ],
        "quick": [
            ("p", "Install the release-candidate build and start Friction. User documentation is at <a href=\"https://friction.graphics/documentation\">friction.graphics/documentation</a>."),
        ],
    },
    {
        "slug": "comfyui",
        "name": "ComfyUI",
        "cat": "ai",
        "url": "https://github.com/Comfy-Org/ComfyUI",
        "license": "GPL-3.0",
        "stars": "143.2k",
        "pushed": "2026-10-26",
        "stack": "Python",
        "best": "Node UI that runs Wan, LTX, Hunyuan and other video models (v0.42.1, 19 Oct 2026)",
        "caveat": "Each model keeps its own license; needs a capable GPU",
        "docs": [
            ("Desktop download", "https://www.comfy.org/download"),
            ("comfy-cli", "https://docs.comfy.org/comfy-cli/getting-started"),
            ("Manual install", "https://github.com/Comfy-Org/ComfyUI#manual-install-windows-linux"),
        ],
        "install": [
            ("p", "The README recommends the <a href=\"https://www.comfy.org/download\">desktop app</a> for Windows and Mac. Portable Windows archives are also linked (Nvidia, AMD, Intel, and an older Nvidia CUDA 12.6 build for 10-series GPUs). The Nvidia portable build it describes ships Python 3.13 and PyTorch CUDA 13.0 and supports 20-series and newer."),
            ("h3", "comfy-cli"),
            ("code", "pip install comfy-cli\ncomfy install"),
            ("h3", "Manual install"),
            ("p", "The README says to git clone the repo. Python 3.13 is “very well supported”; 3.14 works with possible custom-node issues. Nvidia PyTorch, then dependencies:"),
            ("code", "git clone https://github.com/Comfy-Org/ComfyUI.git\ncd ComfyUI\npip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130\npip install -r requirements.txt\npython main.py"),
            ("p", "AMD, Intel, and Apple silicon commands are in the same Installing section (ROCm, XPU, and the Apple PyTorch nightly note). They are not copied in full here. A GPU is required for practical video models; the README also says each model has its own license."),
            src("Commands from the ComfyUI README, checked 26 Oct 2026. The clone URL is the repository this catalog links."),
        ],
        "quick": [
            ("p", "The desktop app or <code>python main.py</code> opens the node graph in a browser. Put checkpoints in <code>models/checkpoints</code>. Video models such as Wan are separate downloads."),
        ],
    },
    {
        "slug": "open-sora",
        "name": "Open-Sora",
        "cat": "ai",
        "url": "https://github.com/hpcaitech/Open-Sora",
        "license": "Apache-2.0",
        "stars": "29.9k",
        "pushed": "2026-04-09",
        "stack": "Python",
        "best": "Fully open model including training code (Open-Sora 2.0, 11B)",
        "caveat": "No new model since 2.0 in Mar 2025",
        "docs": [
            ("README", "https://github.com/hpcaitech/Open-Sora#quickstart"),
            ("Weights", "https://huggingface.co/hpcai-tech/Open-Sora-v2"),
        ],
        "install": [
            ("p", "The README’s quickstart uses conda, Python 3.10, and PyTorch &gt;= 2.4.0. <code>xformers</code> is pinned for CUDA 12.1 in the example; the comment says to match your CUDA version."),
            ("code", "conda create -n opensora python=3.10\nconda activate opensora\ngit clone https://github.com/hpcaitech/Open-Sora\ncd Open-Sora\npip install -v .\npip install xformers==0.0.27.post2 --index-url https://download.pytorch.org/whl/cu121\npip install flash-attn --no-build-isolation"),
            ("p", "Weights:"),
            ("code", "pip install \"huggingface_hub[cli]\"\nhuggingface-cli download hpcai-tech/Open-Sora-v2 --local-dir ./ckpts"),
            ("p", "The README’s efficiency table is measured on H100/H800 GPUs. It does not state a minimum consumer-GPU size in the install section."),
            src("Commands from the Open-Sora README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "One-GPU 256px text-to-video example from the README, with offloading:"),
            ("code", "torchrun --nproc_per_node 1 --standalone scripts/diffusion/inference.py configs/diffusion/inference/t2i2v_256px.py --save-dir samples --prompt \"raining, sea\" --offload True"),
        ],
    },
    {
        "slug": "liveportrait",
        "name": "LivePortrait",
        "cat": "ai",
        "url": "https://github.com/KlingAIResearch/LivePortrait",
        "license": "MIT (code)",
        "stars": "19.3k",
        "pushed": "2026-06-01",
        "stack": "Python",
        "best": "Animating a still portrait from a driving video",
        "caveat": "Repo moved to KlingAIResearch; check bundled model licenses",
        "docs": [("README", "https://github.com/KlingAIResearch/LivePortrait#getting-started-")],
        "install": [
            ("p", "The README requires git, conda, and FFmpeg. It still tells you to clone <code>KlingTeam/LivePortrait</code>. This catalog’s GitHub link is <code>KlingAIResearch/LivePortrait</code>, which is where the repository lives after the move noted in the research."),
            ("code", "git clone https://github.com/KlingTeam/LivePortrait\ncd LivePortrait\nconda create -n LivePortrait python=3.10\nconda activate LivePortrait\npip install -r requirements.txt"),
            ("p", "Linux and Windows: the README shows example PyTorch installs for CUDA 11.1, 11.8, and 12.1, and says to match <code>nvcc -V</code>. Animals mode needs X-Pose; humans mode can skip that CUDA check. macOS Apple Silicon uses <code>pip install -r requirements_macOS.txt</code> and does not support animals mode. Intel macOS is not tested."),
            ("p", "Weights:"),
            ("code", "huggingface-cli download KlingTeam/LivePortrait --local-dir pretrained_weights --exclude \"*.git*\" \"README.md\" \"docs\""),
            src("Commands from the LivePortrait README on KlingAIResearch/LivePortrait, checked 26 Oct 2026. Model files may have their own licenses."),
        ],
        "quick": [
            ("code", "python inference.py"),
            ("p", "On Apple Silicon the README uses <code>PYTORCH_ENABLE_MPS_FALLBACK=1 python inference.py</code> and says it may be about 20× slower than an RTX 4090. A successful run writes <code>animations/s6--d0_concat.mp4</code>."),
        ],
    },
    {
        "slug": "wan22",
        "name": "Wan 2.2",
        "cat": "ai",
        "url": "https://github.com/Wan-Video/Wan2.2",
        "license": "Apache-2.0",
        "stars": "18.2k",
        "pushed": "2026-09-21",
        "stack": "Python",
        "best": "Text/image-to-video, Wan2.2-Animate character animation, speech-to-video",
        "caveat": "14B models need large GPUs; the 5B TI2V model targets a 4090-class card",
        "docs": [
            ("README", "https://github.com/Wan-Video/Wan2.2#run-wan22"),
            ("TI2V-5B weights", "https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B"),
        ],
        "install": [
            ("p", "The README says <code>torch &gt;= 2.4.0</code>. If <code>flash_attn</code> fails, install the other packages first."),
            ("code", "git clone https://github.com/Wan-Video/Wan2.2.git\ncd Wan2.2\npip install -r requirements.txt"),
            ("p", "Speech-to-video with CosyVoice also needs <code>pip install -r requirements_s2v.txt</code>. Download one checkpoint, for example the 5B model:"),
            ("code", "pip install \"huggingface_hub[cli]\"\nhuggingface-cli download Wan-AI/Wan2.2-TI2V-5B --local-dir ./Wan2.2-TI2V-5B"),
            ("p", "GPU notes written in the README: the single-GPU 14B text-to-video command needs at least 80 GB VRAM. The TI2V-5B command below can run on a GPU with at least 24 GB VRAM, and the README gives an RTX 4090 as the example. The 5B model is described as runnable on consumer cards such as a 4090."),
            src("Commands and VRAM notes from the Wan2.2 README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("code", "python generate.py --task ti2v-5B --size 1280*704 --ckpt_dir ./Wan2.2-TI2V-5B --offload_model True --convert_model_dtype --t5_cpu --prompt \"Two anthropomorphic cats in comfy boxing gear and bright gloves fight intensely on a spotlighted stage\""),
        ],
    },
    {
        "slug": "framepack",
        "name": "FramePack",
        "cat": "ai",
        "url": "https://github.com/lllyasviel/FramePack",
        "license": "Apache-2.0",
        "stars": "17.3k",
        "pushed": "2025-10-16",
        "stack": "Python",
        "best": "Practical image-to-video diffusion on consumer GPUs",
        "caveat": "No pushes since Oct 2025",
        "docs": [("README", "https://github.com/lllyasviel/FramePack#installation")],
        "install": [
            ("p", "README requirements: Nvidia GPU in the RTX 30, 40, or 50 series with fp16 and bf16. GTX 10 and RTX 20 series are not tested. Linux or Windows. At least 6 GB of GPU memory. The README says a 60-second 30 fps clip with the 13B model can run in 6 GB."),
            ("h3", "Windows"),
            ("p", "One-click package (CUDA 12.6 + PyTorch 2.6) linked from the README:"),
            ("code", "https://github.com/lllyasviel/FramePack/releases/download/windows/framepack_cu126_torch26.7z"),
            ("p", "Uncompress, run <code>update.bat</code>, then <code>run.bat</code>. The README says the first run downloads more than 30 GB of models."),
            ("h3", "Linux"),
            ("code", "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126\npip install -r requirements.txt\npython demo_gradio.py"),
            ("p", "The README recommends a separate Python 3.10. It says to try the default PyTorch attention before optional kernels such as <code>pip install sageattention==1.0.6</code>."),
            src("Requirements and commands from the FramePack README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "The Gradio GUI is the quick start. The README documents <code>--share</code>, <code>--port</code>, and <code>--server</code> on <code>demo_gradio.py</code>."),
        ],
    },
    {
        "slug": "cogvideox",
        "name": "CogVideoX",
        "cat": "ai",
        "url": "https://github.com/zai-org/CogVideo",
        "license": "Apache-2.0 (code)",
        "stars": "13.1k",
        "pushed": "2025-11-04",
        "stack": "Python",
        "best": "Text/image-to-video research models",
        "caveat": "Weights may carry their own license; check before commercial use",
        "docs": [("README", "https://github.com/zai-org/CogVideo#quick-start")],
        "install": [
            ("p", "The README says Python must be between 3.10 and 3.12 inclusive for both the SAT and Diffusers paths. Diffusers install shown there:"),
            ("code", "pip install -r requirements.txt"),
            ("p", "Then follow <code>inference/cli_demo.py</code>. SAT inference is a separate tree in <code>sat/README.md</code>; the README does not repeat those commands in the quick start."),
            ("p", "GPU notes in the README: CogVideoX-2B can run on older GPUs such as a GTX 1080 Ti, and CogVideoX-5B on desktop GPUs such as an RTX 3060, if you follow <code>requirements.txt</code>. It also says the memory table was measured on NVIDIA A100 / H100 and that turning off CPU offload multiplies memory use. The README says the CogVideoX-2B weights were changed to Apache 2.0; other weights may differ."),
            src("Install line and GPU notes from the CogVideo README, checked 26 Oct 2026. Clone first if you are not already in the repo: <code>git clone https://github.com/zai-org/CogVideo</code>."),
        ],
        "quick": [
            ("p", "The README treats prompt rewriting as part of getting a good result and points at <code>inference/convert_demo.py</code> before <code>inference/cli_demo.py</code>. There is no single one-line generate command in the quick-start section."),
        ],
    },
    {
        "slug": "animatediff",
        "name": "AnimateDiff",
        "cat": "ai",
        "url": "https://github.com/guoyww/AnimateDiff",
        "license": "Apache-2.0",
        "stars": "12.3k",
        "pushed": "2024-07-31",
        "stack": "Python",
        "best": "Motion modules for Stable Diffusion image models",
        "caveat": "Stalled since Jul 2024; superseded by native video models",
        "docs": [
            ("README", "https://github.com/guoyww/AnimateDiff#quick-start"),
            ("Diffusers", "https://huggingface.co/docs/diffusers/api/pipelines/animatediff"),
        ],
        "install": [
            ("p", "The README also points at the Diffusers tutorial. For this repository:"),
            ("code", "git clone https://github.com/guoyww/AnimateDiff.git\ncd AnimateDiff\npip install -r requirements.txt"),
            ("p", "The README says checkpoints download automatically the first time a script runs. It does not state a GPU size or CUDA version in the quick start."),
            src("Commands from the AnimateDiff README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("code", "python -m scripts.animate --config configs/prompts/1_animate/1_1_animate_RealisticVision.yaml"),
            ("p", "Samples are written to <code>samples/</code>."),
        ],
    },
    {
        "slug": "ltx-video",
        "name": "LTX-Video",
        "cat": "ai",
        "url": "https://github.com/Lightricks/LTX-Video",
        "license": "Apache-2.0",
        "stars": "11.2k",
        "pushed": "2026-01-05",
        "stack": "Python",
        "best": "Earlier, permissively licensed LTX model",
        "caveat": "Superseded by LTX-2",
        "docs": [
            ("README", "https://github.com/Lightricks/LTX-Video#quick-start-guide"),
            ("Diffusers", "https://huggingface.co/docs/diffusers/main/en/api/pipelines/ltx_video"),
            ("ComfyUI", "https://github.com/Lightricks/ComfyUI-LTXVideo/"),
        ],
        "install": [
            ("p", "The README says this codebase was tested with Python 3.10.5 and CUDA 12.2, and supports PyTorch &gt;= 2.1.2. On macOS, MPS was tested with PyTorch 2.3.0 and should support PyTorch == 2.3 or &gt;= 2.6."),
            ("code", "git clone https://github.com/Lightricks/LTX-Video.git\ncd LTX-Video\npython -m venv env\nsource env/bin/activate\npython -m pip install -e .[inference]"),
            ("p", "On some shells the extras bracket must be quoted: <code>pip install -e \".[inference]\"</code>. The README writes it as <code>.\\[inference]</code> inside a bash fence. Optional FP8 kernels are a separate repository, for Ada and later."),
            src("Steps from the LTX-Video README, checked 26 Oct 2026. The README says LTX-2 has replaced this line of models."),
        ],
        "quick": [
            ("p", "The README recommends the ComfyUI workflow for quality. The local script it shows:"),
            ("code", "python inference.py --prompt \"PROMPT\" --conditioning_media_paths IMAGE_PATH --conditioning_start_frames 0 --height HEIGHT --width WIDTH --num_frames NUM_FRAMES --seed SEED --pipeline_config configs/ltxv-13b-0.9.8-distilled.yaml"),
        ],
    },
    {
        "slug": "wangp",
        "name": "WanGP",
        "cat": "ai",
        "url": "https://github.com/deepbeepmeep/WanGP",
        "license": "WanGP Community License 2.0",
        "stars": "11.1k",
        "pushed": "2026-10-25",
        "stack": "Python",
        "best": "Low-VRAM app for Wan, LTX, Hunyuan and more",
        "caveat": "Free to use, but no reselling or paid hosting without a commercial license",
        "docs": [
            ("Installation guide", "https://github.com/deepbeepmeep/WanGP/blob/main/docs/INSTALLATION.md"),
            ("AMD", "https://github.com/deepbeepmeep/WanGP/blob/main/docs/AMD-INSTALLATION.md"),
            ("Getting started", "https://github.com/deepbeepmeep/WanGP/blob/main/docs/GETTING_STARTED.md"),
            ("License", "https://github.com/deepbeepmeep/WanGP/blob/main/LICENSE.txt"),
        ],
        "install": [
            ("p", "The README says some models run with as little as <strong>6 GB of VRAM</strong>, and that AMD RDNA 4, 3, 3.5, and 2 are supported. One-click scripts: <code>scripts/install.bat</code> or <code>scripts/install.sh</code>, then <code>scripts/run.bat</code> or <code>scripts/run.sh</code>."),
            ("p", "Manual install for RTX 20-series through 50-series, as printed in the README. The clone URL in the README is <code>Wan2GP.git</code> (the GitHub repository is <code>WanGP</code>):"),
            ("code", "git clone https://github.com/deepbeepmeep/Wan2GP.git\ncd Wan2GP\nconda create -n wan2gp python=3.11.14\nconda activate wan2gp\npip install torch==2.10.0 torchvision==0.25.0 torchaudio==2.10.0 --index-url https://download.pytorch.org/whl/cu130\npip install -r requirements.txt"),
            ("p", "GTX 10-series in the README uses Python 3.10.9 and a different PyTorch build:"),
            ("code", "pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/test/cu128\npip install -r requirements.txt"),
            ("p", "Windows Triton commands are a table in the README (3.6.x with PyTorch 2.10 on RTX 30–50, 3.2.x on RTX 20). AMD steps are in <code>docs/AMD-INSTALLATION.md</code>, not repeated here."),
            src("Commands from the WanGP README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("code", "python wgp.py"),
            ("p", "The README says the Guides tab lists recommended models on first launch, and that disabling browser GPU use can free VRAM."),
        ],
    },
    {
        "slug": "ltx-2",
        "name": "LTX-2",
        "cat": "ai",
        "url": "https://github.com/Lightricks/LTX-2",
        "license": "LTX-2.x Community License",
        "stars": "9.9k",
        "pushed": "2026-10-18",
        "stack": "Python",
        "best": "Video generation with synchronized audio (LTX-2.5 weights, v1.5.0)",
        "caveat": "Entities with $10M+ annual revenue need a paid license",
        "docs": [
            ("README", "https://github.com/Lightricks/LTX-2#quick-start"),
            ("Weights", "https://huggingface.co/Lightricks/LTX-2.5"),
            ("License", "https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x"),
            ("ComfyUI", "https://github.com/Lightricks/ComfyUI-LTXVideo/"),
        ],
        "install": [
            ("p", "The README quick start uses <code>uv</code>. The <code>natten</code> extra is the fastest video-VAE backend and is Linux + CUDA only; on Windows and macOS it is skipped. The distilled LTX-2.5 download is about 66 GiB. Hugging Face may require you to accept the model terms and log in."),
            ("code", "git clone https://github.com/Lightricks/LTX-2.git\ncd LTX-2\nuv sync --extra natten\nhf auth login\nhf download Lightricks/LTX-2.5 \\\n    diffusion_models/ltx-2.5-22b-distilled-transformer-bf16.safetensors \\\n    text_encoders/gemma4-12b-with-proj-ltx-2.5-bf16.safetensors \\\n    vae/ltx-2.5-video-vae-bf16.safetensors \\\n    vae/ltx-2.5-audio-vae-bf16.safetensors \\\n    latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors \\\n    --local-dir models/ltx-2.5"),
            ("p", "Low memory, from the README: add <code>--quantization fp8-cast --offload {cpu, disk}</code>. The README does not print a single minimum VRAM number in the quick start."),
            src("Commands from the LTX-2 README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Fast path is <code>uv run python -m ltx_pipelines.distilled</code> with the five checkpoint paths from the download. The README’s example <code>--prompt</code> is a long paragraph; copy it from the Quick Start rather than a shortened stand-in. Production quality is <code>uv run python -m ltx_pipelines.dfr_pipeline</code> after an extra LoRA download, and it uses more VRAM."),
            ("note", "Commercial entities with $10M+ annual revenue need a paid license. See <a href=\"../licenses.html\">Licenses</a>."),
        ],
    },
    {
        "slug": "wanvideo-wrapper",
        "name": "ComfyUI-WanVideoWrapper",
        "cat": "ai",
        "url": "https://github.com/kijai/ComfyUI-WanVideoWrapper",
        "license": "Apache-2.0",
        "stars": "6.7k",
        "pushed": "2026-05-24",
        "stack": "Python",
        "best": "Community Wan nodes for ComfyUI",
        "caveat": "Last push May 2026",
        "docs": [
            ("README", "https://github.com/kijai/ComfyUI-WanVideoWrapper#installation"),
            ("Models", "https://huggingface.co/Kijai/WanVideo_comfy/tree/main"),
        ],
        "install": [
            ("p", "This is a ComfyUI custom-node pack. Install ComfyUI first. The README’s author also writes that native Wan support in ComfyUI should be preferred unless you need a feature that is not upstream yet."),
            ("code", "git clone https://github.com/kijai/ComfyUI-WanVideoWrapper custom_nodes/ComfyUI-WanVideoWrapper\npip install -r custom_nodes/ComfyUI-WanVideoWrapper/requirements.txt"),
            ("p", "Portable Windows, from the README, run inside the portable folder:"),
            ("code", "python_embeded\\python.exe -m pip install -r ComfyUI\\custom_nodes\\ComfyUI-WanVideoWrapper\\requirements.txt"),
            ("p", "The README’s step 1 is “clone this repo into <code>custom_nodes</code>”; the clone command above is that step with the repository URL. Model files are listed on Hugging Face, not installed by pip."),
            src("Dependency commands from the ComfyUI-WanVideoWrapper README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Restart ComfyUI and add the wrapper’s Wan nodes. The README points at <a href=\"https://huggingface.co/Kijai/WanVideo_comfy/tree/main\">Kijai/WanVideo_comfy</a> and an fp8 scaled set for weights."),
        ],
    },
    {
        "slug": "tooncrafter",
        "name": "ToonCrafter",
        "cat": "ai",
        "url": "https://github.com/Doubiiu/ToonCrafter",
        "license": "Apache-2.0",
        "stars": "6.0k",
        "pushed": "2025-03-19",
        "stack": "Python",
        "best": "Generating in-between frames for cartoons",
        "caveat": "Research code; no pushes since Mar 2025",
        "docs": [
            ("README", "https://github.com/Doubiiu/ToonCrafter#setup"),
            ("Weights", "https://huggingface.co/Doubiiu/ToonCrafter/blob/main/model.ckpt"),
        ],
        "install": [
            ("p", "The README recommends Anaconda and pins Python 3.8.5. It does not print a <code>git clone</code> line; clone the repository, then:"),
            ("code", "git clone https://github.com/Doubiiu/ToonCrafter.git\ncd ToonCrafter\nconda create -n tooncrafter python=3.8.5\nconda activate tooncrafter\npip install -r requirements.txt"),
            ("p", "Download <code>model.ckpt</code> from the Hugging Face link in the README and place it at <code>checkpoints/tooncrafter_512_interp_v1/model.ckpt</code>. The model card in the README lists about 24 GB GPU memory on an A100 for the 512 model (about 24–27 GB in this implementation; a community build lowered that toward 10 GB)."),
            src("Environment commands and memory note from the ToonCrafter README, checked 26 Oct 2026. The clone line adds the repository URL the README assumes you already have."),
        ],
        "quick": [
            ("code", "sh scripts/run.sh"),
            ("p", "Or <code>python gradio_app.py</code> after the checkpoint is in place. The README says clips are up to 16 frames at 512×320."),
        ],
    },
    {
        "slug": "hunyuanvideo",
        "name": "HunyuanVideo 1.5",
        "cat": "ai",
        "url": "https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5",
        "license": "Tencent Hunyuan Community License",
        "stars": "4.6k",
        "pushed": "2026-04-10",
        "stack": "Python",
        "best": "8.3B text/image-to-video; 14 GB minimum with offloading",
        "caveat": "License does not apply in the EU, UK or South Korea",
        "docs": [
            ("README", "https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5#dependencies-and-installation"),
            ("License", "https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE"),
            ("Checkpoints", "https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/checkpoints-download.md"),
        ],
        "install": [
            ("p", "README hardware: NVIDIA GPU with CUDA. Minimum GPU memory is <strong>14 GB with model offloading</strong>. More memory can turn offloading off. Software: <strong>Linux</strong>, Python 3.10 or higher, and a CUDA build that matches PyTorch. The README does not document Windows or macOS installs."),
            ("code", "git clone https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5.git\ncd HunyuanVideo-1.5\npip install -r requirements.txt\npip install -i https://mirrors.tencent.com/pypi/simple/ --upgrade tencentcloud-sdk-python"),
            ("p", "Flash Attention, Flex-Block-Attention, SageAttention, and <code>sgl-kernel==0.3.18</code> are optional speedups with their own commands in the README. Download weights using <code>checkpoints-download.md</code> before generating."),
            src("Requirements and commands from the HunyuanVideo-1.5 README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Inference commands are in the README’s “Inference with Source Code” section and depend on which checkpoint you downloaded (480p text-to-video and image-to-video are linked from the model cards). This page does not copy a command that only works after a specific checkpoint layout."),
            ("note", "The Tencent Hunyuan Community License does not apply in the EU, the UK, or South Korea. See <a href=\"../licenses.html\">Licenses</a>."),
        ],
    },
    {
        "slug": "lottie-web",
        "name": "lottie-web",
        "cat": "lottie",
        "url": "https://github.com/airbnb/lottie-web",
        "license": "MIT",
        "stars": "32.3k",
        "pushed": "2025-09-01",
        "stack": "JavaScript",
        "best": "Playing After Effects-exported Lottie animations",
        "caveat": "No video export; render frames through a code-driven pipeline",
        "docs": [
            ("Docs", "https://airbnb.io/lottie/"),
            ("npm", "https://www.npmjs.com/package/lottie-web"),
        ],
        "install": [
            ("p", "For playback in a web page, the README’s HTML player install is:"),
            ("code", "npm install lottie-web"),
            ("p", "It also mentions <code>bower install bodymovin</code> and a cdnjs build. The After Effects exporter (Bodymovin) is a separate plugin; the README’s preferred install is the aescripts listing, with a Homebrew cask path <code>brew tap danielbayley/adobe</code> then <code>brew cask install lottie</code>. That plugin is not required to play a JSON file you already have."),
            src("npm command from the lottie-web README, checked 26 Oct 2026."),
        ],
        "quick": [
            ("p", "Include the player and load a JSON animation. The README’s usage section starts with <code>lottie.loadAnimation({...})</code>. There is no MP4 export in this library; to get a video file, render frames in another tool from this catalog."),
        ],
    },
]


PICKS = [
    {
        "rank": 1,
        "title": "HyperFrames",
        "why": "Agent-written HTML to MP4; most-starred code-driven tool here",
        "license": "Apache-2.0",
        "cats": "code",
        "href": "tools/hyperframes.html",
    },
    {
        "rank": 2,
        "title": "Remotion",
        "why": "Mature React video pipeline for templated content at scale",
        "license": "Source-available",
        "cats": "code",
        "href": "tools/remotion.html",
    },
    {
        "rank": 3,
        "title": "Blender",
        "why": "3D, 2D Grease Pencil, compositing and editing in one app",
        "license": "GPL-2.0+",
        "cats": "apps",
        "href": "tools/blender.html",
    },
    {
        "rank": 4,
        "title": "ComfyUI",
        "why": "Local AI video and character animation, permissive weights. Wan 2.2 (Apache-2.0) is the model in this pick.",
        "license": "GPL-3.0",
        "cats": "ai",
        "href": "tools/comfyui.html",
    },
    {
        "rank": 5,
        "title": "Manim (Community)",
        "why": "Math and technical explainers in Python",
        "license": "MIT",
        "cats": "pipeline",
        "href": "tools/manim.html",
    },
    {
        "rank": 6,
        "title": "LTX-2",
        "why": "AI video with synchronized audio",
        "license": "Community license",
        "cats": "ai",
        "href": "tools/ltx-2.html",
    },
    {
        "rank": 7,
        "title": "Motion Canvas",
        "why": "MIT-licensed code animation with a visual editor",
        "license": "MIT",
        "cats": "code",
        "href": "tools/motion-canvas.html",
    },
    {
        "rank": 8,
        "title": "OpenToonz",
        "why": "Production 2D cel and cut-out animation",
        "license": "BSD-3-Clause",
        "cats": "apps",
        "href": "tools/opentoonz.html",
    },
    {
        "rank": 9,
        "title": "Friction",
        "why": "After Effects-style vector motion graphics (enve fork)",
        "license": "GPL-3.0",
        "cats": "motion",
        "href": "tools/friction.html",
    },
]


def search_blob(tool):
    parts = [
        tool["name"],
        tool["best"],
        tool["license"],
        tool["stack"],
        tool["caveat"],
        CAT_NAME[tool["cat"]],
        tool["stars"],
    ]
    # Keep the previous section name findable after the breadcrumb rename.
    if tool["cat"] == "ai":
        parts.append("AI generative")
    return " ".join(parts)


def nav(prefix, current):
    items = [
        ("home", "Home", f"{prefix}index.html"),
        ("picks", "Top picks", f"{prefix}index.html#top-picks"),
    ]
    for cid, _name, label, _blurb in CATEGORIES:
        items.append((cid, label, f"{prefix}index.html#{cid}"))
    items.append(("licenses", "Licenses", f"{prefix}licenses.html"))
    items.append(("choose", "How to choose", f"{prefix}choose.html"))
    links = []
    for key, label, href in items:
        current_attr = ' aria-current="page"' if key == current else ""
        links.append(f'<a href="{e(href)}"{current_attr}>{e(label)}</a>')
    return "\n".join(links)


def page(prefix, current, title, body, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <link rel="stylesheet" href="{prefix}css/site.css">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect fill='%23145c40' width='32' height='32' rx='6'/%3E%3Crect fill='%23f4f1ea' x='7' y='8' width='18' height='16' rx='2'/%3E%3C/svg%3E">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{prefix}index.html">
        <strong>Animated 2026</strong>
        <span>Open tools for video</span>
      </a>
      <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav">
        <span data-label-closed>Menu</span>
        <span data-label-open>Close</span>
      </button>
      <nav class="nav" id="site-nav" aria-label="Primary">
        {nav(prefix, current)}
      </nav>
      <button class="theme-btn" type="button" data-theme-toggle aria-label="Theme: system">System</button>
    </div>
  </header>
  <main id="main">
    <div class="wrap">
      {body}
    </div>
  </main>
  <footer class="site-footer">
    <div class="wrap">
      <p>Data as of {AS_OF}. Stars and last push from the GitHub API. Not a live count.</p>
      <p><a href="{prefix}notes.html">Sources and notes</a></p>
    </div>
  </footer>
  <script src="{prefix}js/site.js"></script>
</body>
</html>
"""


def tool_card(tool, prefix):
    return f"""<article class="tool" data-tool data-cat="{e(tool["cat"])}" data-search="{e(search_blob(tool))}">
  <h3><a href="{prefix}tools/{e(tool["slug"])}.html">{e(tool["name"])}</a></h3>
  <p class="best">{e(tool["best"])}</p>
  <ul class="meta">
    <li>{e(tool["license"])}</li>
    <li>{e(tool["stars"])} stars</li>
    <li>Push {e(tool["pushed"])}</li>
  </ul>
</article>"""


def index_body():
    pick_cards = []
    for pick in PICKS:
        search = " ".join([pick["title"], pick["why"], pick["license"]])
        pick_cards.append(
            f"""<article class="card" data-tool data-cat="{e(pick["cats"])}" data-search="{e(search)}">
  <p class="rank">Top pick {pick["rank"]}</p>
  <h3><a href="{e(pick["href"])}">{e(pick["title"])}</a></h3>
  <p class="best">{e(pick["why"])}</p>
  <ul class="meta"><li>{e(pick["license"])}</li></ul>
</article>"""
        )
    chips = ['<button type="button" data-filter="all" aria-pressed="true">All</button>']
    for cid, _name, label, _blurb in CATEGORIES:
        chips.append(
            f'<button type="button" data-filter="{cid}" aria-pressed="false">{e(label)}</button>'
        )
    sections = []
    for cid, name, _label, blurb in CATEGORIES:
        cards = "\n".join(tool_card(t, "") for t in TOOLS if t["cat"] == cid)
        sections.append(
            f"""<section class="section" id="{cid}" data-section>
  <div class="section-head">
    <h2>{e(name)}</h2>
    <p class="muted">{e(blurb)}</p>
  </div>
  <div class="tool-grid">
    {cards}
  </div>
</section>"""
        )
    return f"""<p class="kicker">Catalog as of {AS_OF}</p>
<h1>Open-source tools for animated video</h1>
<div class="lede">
  <p>35 open-source and source-available tools for animated video. Stars and last push are from the GitHub API on 26 Oct 2026.</p>
  <p>The biggest shift in 2026 is agent-driven video: HyperFrames, HeyGen’s Apache-2.0 HTML-to-video framework, already has 72.9k stars and shipped v0.8.206 on 26 Oct 2026. For generated footage, Wan 2.2 inside ComfyUI is the most permissive strong option in this set.</p>
  <p class="muted">Each tool page has install steps copied from that project’s README or the official docs the README points to. Nothing here is a company product, and there are no testimonials.</p>
</div>
<section class="section" id="top-picks" data-section data-count="skip">
  <div class="section-head">
    <h2>Top picks</h2>
    <p class="muted"><a href="choose.html">How to choose</a> · <a href="licenses.html">License gotchas</a></p>
  </div>
  <div class="cards">
    {"".join(pick_cards)}
  </div>
</section>
<section class="section" id="catalog">
  <h2>All tools</h2>
  <div class="controls">
    <div>
      <label for="q">Search tools</label>
      <input id="q" type="search" placeholder="Name, license, stack, or what it’s for" autocomplete="off">
    </div>
    <div>
      <p id="filters-label" class="control-label">Category</p>
      <div class="filters" role="group" aria-labelledby="filters-label">
        {"".join(chips)}
      </div>
    </div>
    <p id="count" aria-live="polite">35 tools</p>
    <div class="empty" id="none" hidden>
      <p>No tools match this search or category.</p>
      <button type="button" class="clear-filters" data-clear-filters>Clear filters</button>
    </div>
  </div>
  {"".join(sections)}
</section>"""


def sentence(text):
    text = str(text).strip()
    if text and text[-1] not in ".!?":
        text += "."
    return text


def overview_html(tool):
    """Purpose plus stack, then the recorded caveat. No claims beyond catalog fields."""
    best = tool["best"].strip().rstrip(".")
    stack = tool["stack"].strip().rstrip(".")
    return f"<p>{e(sentence(best + ' — ' + stack))} {e(sentence(tool['caveat']))}</p>"


def crumb_nav(parts):
    lis = []
    for i, (label, href) in enumerate(parts):
        if i:
            lis.append('    <li aria-hidden="true">/</li>')
        if href:
            lis.append(f'    <li><a href="{e(href)}">{e(label)}</a></li>')
        else:
            lis.append(f'    <li aria-current="page">{e(label)}</li>')
    inner = "\n".join(lis)
    return (
        '<nav aria-label="Breadcrumb">\n'
        '  <ol class="crumb">\n'
        f"{inner}\n"
        "  </ol>\n"
        "</nav>"
    )


def tool_page(tool):
    cat_id = tool["cat"]
    docs = "".join(f'<li><a href="{e(href)}">{e(label)}</a></li>' for label, href in tool["docs"])
    docs = f'<li><a href="{e(tool["url"])}">GitHub</a></li>' + docs
    crumbs = crumb_nav(
        [
            ("Home", "../index.html"),
            (CAT_NAME[cat_id], f"../index.html#{cat_id}"),
            (tool["name"], None),
        ]
    )
    body = f"""{crumbs}
<p class="kicker">{e(CAT_NAME[cat_id])}</p>
<h1>{e(tool["name"])}</h1>
<p class="lede">{e(tool["best"])}</p>
<dl class="facts">
  <div><dt>License</dt><dd>{e(tool["license"])}</dd></div>
  <div><dt>Stars</dt><dd>{e(tool["stars"])}</dd></div>
  <div><dt>Last push</dt><dd>{e(tool["pushed"])}</dd></div>
  <div><dt>Stack</dt><dd>{e(tool["stack"])}</dd></div>
</dl>
<div class="prose">
  <h2>Overview</h2>
  {overview_html(tool)}
  <h2>Install</h2>
  {blocks(tool["install"])}
  <h2>Quick start</h2>
  {blocks(tool["quick"])}
  <h2>Caveats</h2>
  <p class="callout">{e(tool["caveat"])}</p>
  <h2>Links</h2>
  <ul class="links">{docs}</ul>
</div>"""
    desc = f"{tool['name']}: {tool['best']}. License {tool['license']}. Install notes as of {AS_OF}."
    return page("../", "", f"{tool['name']} · Animated 2026", body, desc)


def licenses_body():
    return crumb_nav([("Home", "index.html"), ("License gotchas", None)]) + """
<p class="kicker">From the 26 Oct 2026 research notes</p>
<h1>License gotchas</h1>
<p class="lede">Using these tools to make a video is often less restricted than shipping the tool or the model weights. The notes below are the ones that change a buying or shipping decision. They are not legal advice.</p>
<article class="gotcha">
  <h2>Remotion</h2>
  <p>Remotion License: free for individuals, non-profits, and for-profits up to 3 employees. Larger companies need a company license. The planned v5 license also counts contractors toward team size.</p>
  <p><a href="https://github.com/remotion-dev/remotion/blob/main/LICENSE.md">LICENSE.md</a> · <a href="https://github.com/remotion-dev/remotion/pull/3750">v5 license change (PR 3750)</a></p>
</article>
<article class="gotcha">
  <h2>LTX-2</h2>
  <p>LTX-2.x Community License: commercial entities with $10M+ annual revenue need a paid commercial license.</p>
  <p><a href="https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x">LICENSE-2_x</a></p>
</article>
<article class="gotcha">
  <h2>HunyuanVideo 1.5</h2>
  <p>Tencent Hunyuan Community License: does not apply in the EU, UK, or South Korea, and has an acceptable-use policy.</p>
  <p><a href="https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE">License</a></p>
</article>
<article class="gotcha">
  <h2>WanGP</h2>
  <p>WanGP Community License 2.0: free to use and sell outputs. No reselling, white-labeling, or paid hosting of the app itself without a commercial license.</p>
  <p><a href="https://github.com/deepbeepmeep/WanGP/blob/main/LICENSE.txt">LICENSE.txt</a></p>
</article>
<article class="gotcha">
  <h2>GPL apps</h2>
  <p>ComfyUI, Blender, Kdenlive, and the other GPL apps: using them to make videos is unrestricted. The copyleft only matters if you redistribute modified code.</p>
</article>
<article class="gotcha">
  <h2>Code versus model weights</h2>
  <p>An Apache or MIT code license on CogVideoX, LivePortrait, or a ComfyUI workflow does not cover the model weights or bundled third-party models. Check each weight file before commercial use.</p>
</article>
<article class="gotcha">
  <h2>Also in a project README</h2>
  <p>Diffusion Studio Core is listed here as MPL-2.0. Its README, checked 26 Oct 2026, says rendered video keeps a “Made with Diffusion Studio” watermark unless you buy a license key. That condition is not in the summary table above.</p>
  <p><a href="tools/diffusion-studio.html">Diffusion Studio Core</a></p>
</article>"""


def choose_body():
    return crumb_nav([("Home", "index.html"), ("How to choose", None)]) + """
<p class="kicker">From the 26 Oct 2026 research notes</p>
<h1>How to choose</h1>
<p class="lede">Match the kind of picture to a path already in this catalog. The table is the short version. The list below is the same choice, by job.</p>
<div class="table-wrap">
<table class="decision">
  <caption>Code-driven, desktop apps, motion graphics, or AI video</caption>
  <thead>
    <tr>
      <th scope="col">You are making</th>
      <th scope="col">Open</th>
      <th scope="col">In this catalog</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td data-label="You are making">A video described in code, HTML, or by an agent</td>
      <td data-label="Open"><a href="index.html#code">Code-driven</a></td>
      <td data-label="In this catalog"><a href="tools/hyperframes.html">HyperFrames</a> if you think in HTML/CSS. <a href="tools/remotion.html">Remotion</a> if you are a React team and fine with its license. <a href="tools/motion-canvas.html">Motion Canvas</a> or <a href="tools/revideo.html">Revideo</a> for MIT.</td>
    </tr>
    <tr>
      <td data-label="You are making">Explainers, diagrams, math, encoding, or batch edits</td>
      <td data-label="Open"><a href="index.html#pipeline">Pipeline &amp; CLI</a></td>
      <td data-label="In this catalog"><a href="tools/manim.html">Manim Community</a> for math. <a href="tools/ffmpeg.html">FFmpeg</a> for encoding and batch jobs. <a href="tools/moviepy.html">MoviePy</a> for scripted cutting, compositing, captions and titles. <a href="tools/editly.html">editly</a> for a declarative JSON5 spec or CLI to a finished slideshow-style video.</td>
    </tr>
    <tr>
      <td data-label="You are making">Drawing, rigging, cel work, or a 3D scene</td>
      <td data-label="Open"><a href="index.html#apps">2D/3D apps</a></td>
      <td data-label="In this catalog"><a href="tools/opentoonz.html">OpenToonz</a> or <a href="tools/tahoma2d.html">Tahoma2D</a> for production 2D. <a href="tools/synfig.html">Synfig</a> for rigged vector. <a href="tools/krita.html">Krita</a> or <a href="tools/pencil2d.html">Pencil2D</a> for hand-drawn. <a href="tools/blender.html">Blender</a> Grease Pencil for 2D in 3D.</td>
    </tr>
    <tr>
      <td data-label="You are making">Keyframed graphics, a node composite, or the final edit</td>
      <td data-label="Open"><a href="index.html#motion">Motion graphics</a></td>
      <td data-label="In this catalog"><a href="tools/friction.html">Friction</a> for After Effects-style vector work. <a href="tools/natron.html">Natron</a> for node compositing. Blender’s compositor for 3D-heavy shots. <a href="tools/kdenlive.html">Kdenlive</a> or <a href="tools/shotcut.html">Shotcut</a> for editing.</td>
    </tr>
    <tr>
      <td data-label="You are making">Generated shots or character animation</td>
      <td data-label="Open"><a href="index.html#ai">AI video</a></td>
      <td data-label="In this catalog"><a href="tools/comfyui.html">ComfyUI</a> as the workbench with <a href="tools/wan22.html">Wan 2.2</a> (Apache-2.0) first. <a href="tools/ltx-2.html">LTX-2</a> when you need audio. <a href="tools/wangp.html">WanGP</a> on low-VRAM GPUs.</td>
    </tr>
    <tr>
      <td data-label="You are making">Vector playback from an After Effects export</td>
      <td data-label="Open"><a href="index.html#lottie">Lottie &amp; vector</a></td>
      <td data-label="In this catalog"><a href="tools/lottie-web.html">lottie-web</a> plays the exported JSON. No video export; render frames through a code-driven pipeline.</td>
    </tr>
  </tbody>
</table>
</div>
<h2>By job</h2>
<ol class="choose-list prose">
  <li><strong>Videos from data, templates, or AI agents.</strong> <a href="tools/hyperframes.html">HyperFrames</a> if you think in HTML/CSS. <a href="tools/remotion.html">Remotion</a> if you are a React team and fine with its license. <a href="tools/motion-canvas.html">Motion Canvas</a> or <a href="tools/revideo.html">Revideo</a> for MIT.</li>
  <li><strong>Explainers, diagrams, and math.</strong> <a href="tools/manim.html">Manim Community</a>. <a href="tools/motion-canvas.html">Motion Canvas</a> for a visual timeline.</li>
  <li><strong>Character or cel animation.</strong> <a href="tools/opentoonz.html">OpenToonz</a> or <a href="tools/tahoma2d.html">Tahoma2D</a> for production 2D, <a href="tools/synfig.html">Synfig</a> for rigged vector, <a href="tools/krita.html">Krita</a> or <a href="tools/pencil2d.html">Pencil2D</a> for hand-drawn, <a href="tools/blender.html">Blender</a> Grease Pencil for 2D in 3D.</li>
  <li><strong>Motion graphics and compositing.</strong> <a href="tools/friction.html">Friction</a> for After Effects-style vector work, <a href="tools/natron.html">Natron</a> for node compositing, Blender’s compositor for 3D-heavy shots.</li>
  <li><strong>AI-generated shots and animation.</strong> <a href="tools/comfyui.html">ComfyUI</a> as the workbench with <a href="tools/wan22.html">Wan 2.2</a> (Apache-2.0) first. <a href="tools/ltx-2.html">LTX-2</a> when you need audio. <a href="tools/wangp.html">WanGP</a> on low-VRAM GPUs.</li>
  <li><strong>Final assembly.</strong> <a href="tools/kdenlive.html">Kdenlive</a> or <a href="tools/shotcut.html">Shotcut</a> for editing. <a href="tools/ffmpeg.html">FFmpeg</a> underneath for encoding and batch jobs.</li>
</ol>
<p><a href="licenses.html">Read the license gotchas</a> before you ship a product that embeds one of these tools.</p>"""


def notes_body():
    return crumb_nav([("Home", "index.html"), ("Sources and notes", None)]) + """
<p class="kicker">Methodology</p>
<h1>Sources and notes</h1>
<div class="prose">
  <p>This catalog lists 35 tools. Stars and last-push dates were taken from the GitHub API on 26 Oct 2026 and are stored as published in the research notes (for example “72.9k”, not a live recount). Licenses, “best for” lines, stacks, and caveats are from that same pass. This page does not add tools that were left out of it.</p>
  <h2>Install steps</h2>
  <p>Install and quick-start commands were copied from each project’s GitHub README, or from the official install page that README links, on 26 Oct 2026. Where a README has no end-user command, the tool page says so and links the download page that was actually fetched. Commands that could not be read from those pages are not filled in from memory.</p>
  <h2>Stalled or left out</h2>
  <ul>
    <li>Theatre.js: Apache-2.0 motion editor for the web, no pushes since Aug 2024.</li>
    <li>Olive: GPL-3.0 video editor, no pushes since Dec 2024.</li>
    <li>AnimateDiff, ToonCrafter, FramePack, and editly are still listed because they remain usable, but they have no recent pushes. See each tool’s caveat.</li>
    <li>SkyReels-V2 was left out because its license could not be confirmed from the repo.</li>
  </ul>
  <h2>Primary sources</h2>
  <ul>
    <li><a href="https://www.blender.org/releases/5-2/">Blender 5.2 LTS release page</a></li>
    <li><a href="https://github.com/remotion-dev/remotion/blob/main/LICENSE.md">Remotion license</a></li>
    <li><a href="https://github.com/remotion-dev/remotion/pull/3750">Remotion 5.0 license changes (PR 3750)</a></li>
    <li><a href="https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x">LTX-2.x Community License</a></li>
    <li><a href="https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/LICENSE">HunyuanVideo 1.5 license</a></li>
    <li><a href="https://github.com/deepbeepmeep/WanGP/blob/main/LICENSE.txt">WanGP license</a></li>
    <li>GitHub repositories linked on each tool page (GitHub API, 26 Oct 2026)</li>
  </ul>
</div>"""


def squash(text):
    return " ".join(text.split())


def catalog_href(href, up):
    """Rewrite catalog HTML links to relative Markdown paths. External URLs stay put."""
    href = (href or "").strip()
    if not href or href.startswith(("http://", "https://", "mailto:", "#")):
        return href
    climbed = False
    while href.startswith("../"):
        href = href[3:]
        climbed = True
    path, _, anchor = href.partition("#")
    anchor = f"#{anchor}" if anchor else ""
    renamed = {
        "index.html": "README.md",
        "licenses.html": "licenses.md",
        "choose.html": "choose.md",
        "notes.html": "notes.md",
    }
    if path in renamed:
        path = renamed[path]
    elif path.endswith(".html"):
        path = path[:-5] + ".md"
    prefix = up if climbed else ""
    return f"{prefix}{path}{anchor}"


class MDBuilder(HTMLParser):
    """Turn the catalog's small HTML subset into GitHub-flavored Markdown."""

    INLINE = {"a", "strong", "b", "em", "code"}

    def __init__(self, up):
        super().__init__(convert_charrefs=True)
        self.up = up
        self.parts = []
        self.stack = [["root"]]
        self.list_stack = []
        self.table = None
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if self.skip:
            self.skip += 1
            return
        ad = dict(attrs)
        if ad.get("aria-hidden") == "true":
            self.skip = 1
            return
        if tag == "a":
            self.stack.append(["a", ad.get("href", "")])
            return
        if tag in self.INLINE:
            self.stack.append([tag])
            return
        if tag in ("ul", "ol"):
            self.list_stack.append({"tag": tag, "crumb": "crumb" in ad.get("class", ""), "items": []})
            return
        if tag in ("li", "p", "h1", "h2", "h3", "caption", "td", "th"):
            self.stack.append([tag, ad.get("class", "")])
            return
        if tag == "table":
            self.table = {"head": [], "rows": [], "in_head": False, "row": None, "caption": ""}
            return
        if tag == "thead" and self.table:
            self.table["in_head"] = True
            return
        if tag == "tbody" and self.table:
            self.table["in_head"] = False
            return
        if tag == "tr" and self.table:
            self.table["row"] = []
            return

    def handle_endtag(self, tag):
        if self.skip:
            self.skip -= 1
            return
        if tag in self.INLINE or tag in ("li", "p", "h1", "h2", "h3", "caption", "td", "th"):
            if len(self.stack) < 2 or self.stack[-1][0] != tag:
                return
            if tag in ("p", "h1", "h2", "h3", "caption", "li", "td", "th"):
                frame = self.stack.pop()
                self._emit_block(tag, squash("".join(frame[2:])), frame[1])
                return
            self._pop_inline()
            return
        if tag in ("ul", "ol") and self.list_stack:
            lst = self.list_stack.pop()
            items = [item for item in lst["items"] if item]
            if not items:
                return
            if lst["crumb"]:
                self.parts.append(" / ".join(items))
                return
            lines = []
            for i, item in enumerate(items, 1):
                prefix = f"{i}. " if tag == "ol" else "- "
                lines.append(prefix + item)
            self.parts.append("\n".join(lines))
            return
        if tag == "tr" and self.table and self.table["row"] is not None:
            row = self.table["row"]
            if self.table["in_head"]:
                self.table["head"] = row
            else:
                self.table["rows"].append(row)
            self.table["row"] = None
            return
        if tag == "table" and self.table:
            caption = self.table["caption"]
            headers = self.table["head"]
            rows = self.table["rows"]
            if not headers and rows:
                headers = rows.pop(0)
            if caption:
                self.parts.append(f"**{caption}**")
            if headers:
                self.parts.append(render_table(headers, rows))
            self.table = None

    def handle_data(self, data):
        if self.skip or not data:
            return
        self.stack[-1].append(data)

    def _pop_inline(self):
        frame = self.stack.pop()
        kind = frame[0]
        if kind == "a":
            text = squash("".join(frame[2:]))
            rendered = f"[{text}]({catalog_href(frame[1], self.up)})"
        elif kind == "code":
            text = "".join(frame[1:])
            rendered = f"`` {text} ``" if "`" in text else f"`{text}`"
        elif kind in ("strong", "b"):
            rendered = f"**{squash(''.join(frame[1:]))}**"
        elif kind == "em":
            rendered = f"*{squash(''.join(frame[1:]))}*"
        else:
            rendered = squash("".join(frame[1:]))
        self.stack[-1].append(rendered)

    def _emit_block(self, tag, text, cls=""):
        if tag == "li":
            if self.list_stack:
                self.list_stack[-1]["items"].append(text)
            elif text:
                self.parts.append(f"- {text}")
            return
        if tag in ("td", "th") and self.table and self.table["row"] is not None:
            self.table["row"].append(text)
            return
        if tag == "caption" and self.table is not None:
            self.table["caption"] = text
            return
        if not text:
            return
        if tag == "h1":
            self.parts.append(f"# {text}")
        elif tag == "h2":
            self.parts.append(f"## {text}")
        elif tag == "h3":
            self.parts.append(f"### {text}")
        elif tag == "p" and "kicker" in cls:
            self.parts.append(f"*{text}*")
        else:
            self.parts.append(text)

    def markdown(self):
        return "\n\n".join(self.parts).strip() + "\n"


def fragment_to_md(html, up):
    parser = MDBuilder(up)
    parser.feed(html)
    parser.close()
    return parser.markdown()


def inline_to_md(fragment, up):
    return fragment_to_md(f"<p>{fragment}</p>", up).strip()


def render_table(headers, rows):
    def cell(value):
        return value.replace("|", "\\|")

    lines = [
        "| " + " | ".join(cell(col) for col in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        padded = row + [""] * (len(headers) - len(row))
        lines.append("| " + " | ".join(cell(col) for col in padded[: len(headers)]) + " |")
    return "\n".join(lines)


def md_blocks(items, up):
    parts = []
    for kind, payload in items:
        if kind == "p":
            parts.append(inline_to_md(payload, up))
        elif kind == "h3":
            parts.append(f"### {payload}")
        elif kind == "note":
            text = inline_to_md(payload, up)
            parts.append("> **Check this.** " + text)
        elif kind == "ul":
            parts.append("\n".join(f"- {inline_to_md(item, up)}" for item in payload))
        elif kind == "ol":
            parts.append("\n".join(f"{i}. {inline_to_md(item, up)}" for i, item in enumerate(payload, 1)))
        elif kind == "code":
            body = payload.rstrip("\n")
            fence = "````" if "```" in body else "```"
            parts.append(f"{fence}\n{body}\n{fence}")
        else:
            raise ValueError(kind)
    return "\n\n".join(parts)


def root_nav():
    return "[Catalog](README.md) · [How to choose](choose.md) · [Licenses](licenses.md) · [Notes](notes.md)"


def tool_nav():
    return "[Catalog](../README.md) · [How to choose](../choose.md) · [Licenses](../licenses.md) · [Notes](../notes.md)"


def md_overview(tool):
    best = tool["best"].strip().rstrip(".")
    stack = tool["stack"].strip().rstrip(".")
    return f"{sentence(best + ' — ' + stack)} {sentence(tool['caveat'])}"


def readme_md():
    lines = [
        "# Animated 2026",
        "",
        "A catalog of open-source and source-available tools for creating animated videos, as of 26 October 2026. Browse it here, in this repository.",
        "",
        f"{len(TOOLS)} tools, with license, GitHub stars, last push, what each one is for, and install or quick-start steps taken from that project’s official README or the docs the README points to.",
        "",
        "The biggest shift in 2026 is agent-driven video: HyperFrames, HeyGen’s Apache-2.0 HTML-to-video framework, already has 72.9k stars and shipped v0.8.206 on 26 Oct 2026. For generated footage, Wan 2.2 inside ComfyUI is the most permissive strong option in this set.",
        "",
        "Stars and last-push dates come from the GitHub API on 26 Oct 2026. They are not a live count. Nothing here is a company product, and there are no testimonials.",
        "",
        "**Browse:** [How to choose](choose.md) · [License gotchas](licenses.md) · [Sources and notes](notes.md)",
        "",
        '<a id="top-picks"></a>',
        "",
        "## Top picks",
        "",
    ]
    for pick in PICKS:
        href = pick["href"].replace(".html", ".md")
        lines.append(f"{pick['rank']}. **[{pick['title']}]({href})** — {pick['why']} · {pick['license']}")
    lines.extend(["", '<a id="catalog"></a>', "", "## All tools", ""])
    for cid, name, _label, blurb in CATEGORIES:
        lines.extend([f'<a id="{cid}"></a>', "", f"### {name}", "", blurb, ""])
        for tool in TOOLS:
            if tool["cat"] != cid:
                continue
            lines.append(
                f"- [{tool['name']}](tools/{tool['slug']}.md) — {tool['best']} · {tool['license']} · {tool['stars']} stars · push {tool['pushed']}"
            )
        lines.append("")
    lines.extend(
        [
            "---",
            "",
            f"Data as of {AS_OF}. [How to choose](choose.md) · [License gotchas](licenses.md) · [Sources and notes](notes.md)",
            "",
        ]
    )
    return "\n".join(lines)


def tools_index_md():
    lines = [
        tool_nav(),
        "",
        "# Tools",
        "",
        "One page per tool. The grouped list on the [catalog home](../README.md#catalog) is the same set.",
        "",
    ]
    for cid, name, _label, blurb in CATEGORIES:
        lines.extend([f"## {name}", "", blurb, ""])
        for tool in TOOLS:
            if tool["cat"] != cid:
                continue
            lines.append(f"- [{tool['name']}]({tool['slug']}.md) — {tool['best']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def tool_md(tool):
    cat = tool["cat"]
    links = [f"- [GitHub]({tool['url']})"]
    for label, href in tool["docs"]:
        links.append(f"- [{label}]({href})")
    facts = render_table(
        ["Fact", "Recorded value"],
        [
            ["License", tool["license"]],
            ["Stars", tool["stars"]],
            ["Last push", tool["pushed"]],
            ["Stack", tool["stack"]],
        ],
    )
    return "\n".join(
        [
            tool_nav(),
            "",
            f"[Catalog](../README.md) / [{CAT_NAME[cat]}](../README.md#{cat}) / {tool['name']}",
            "",
            f"# {tool['name']}",
            "",
            tool["best"],
            "",
            facts,
            "",
            "## Overview",
            "",
            md_overview(tool),
            "",
            "## Install",
            "",
            md_blocks(tool["install"], "../"),
            "",
            "## Quick start",
            "",
            md_blocks(tool["quick"], "../"),
            "",
            "## Caveats",
            "",
            f"> {tool['caveat']}",
            "",
            "## Links",
            "",
            "\n".join(links),
            "",
        ]
    )


def support_md(body_html):
    return root_nav() + "\n\n" + fragment_to_md(body_html, "")


def write_markdown():
    tools_dir = ROOT / "tools"
    tools_dir.mkdir(parents=True, exist_ok=True)
    (ROOT / "README.md").write_text(readme_md(), encoding="utf-8")
    (ROOT / "choose.md").write_text(support_md(choose_body()), encoding="utf-8")
    (ROOT / "licenses.md").write_text(support_md(licenses_body()), encoding="utf-8")
    (ROOT / "notes.md").write_text(support_md(notes_body()), encoding="utf-8")
    (tools_dir / "README.md").write_text(tools_index_md(), encoding="utf-8")
    for tool in TOOLS:
        (tools_dir / f"{tool['slug']}.md").write_text(tool_md(tool), encoding="utf-8")


def main():
    write_markdown()
    (DOCS / "tools").mkdir(parents=True, exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    desc = "Catalog of open-source and source-available tools for animated video, as of 26 Oct 2026."
    (DOCS / "index.html").write_text(
        page("", "home", "Animated 2026 · open tools for animated video", index_body(), desc),
        encoding="utf-8",
    )
    (DOCS / "licenses.html").write_text(
        page("", "licenses", "License gotchas · Animated 2026", licenses_body(), "License constraints for Remotion, LTX-2, HunyuanVideo, WanGP, GPL apps, and model weights."),
        encoding="utf-8",
    )
    (DOCS / "choose.html").write_text(
        page("", "choose", "How to choose · Animated 2026", choose_body(), "How to pick an open-source animated video tool for the job."),
        encoding="utf-8",
    )
    (DOCS / "notes.html").write_text(
        page("", "notes", "Sources and notes · Animated 2026", notes_body(), "Where the Animated 2026 catalog data and install steps came from."),
        encoding="utf-8",
    )
    for tool in TOOLS:
        path = DOCS / "tools" / f"{tool['slug']}.html"
        path.write_text(tool_page(tool), encoding="utf-8")
    print(f"wrote README, support pages, and {len(TOOLS)} markdown tool pages; refreshed HTML in docs/")


if __name__ == "__main__":
    main()
