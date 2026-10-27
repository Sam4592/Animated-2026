# Animated 2026

A browsable catalog of open-source and source-available tools for creating animated videos, as of 26 October 2026.

The site lists 35 tools with license, GitHub stars, last push, what each one is for, and install or quick-start steps taken from that project’s official README or the docs the README points to. It is a reference catalog, not a product.

Once GitHub Pages is enabled, the site is at [https://sam4592.github.io/Animated-2026/](https://sam4592.github.io/Animated-2026/).

## What’s in the site

- `docs/index.html` — short intro, top picks, and a searchable list by category. A search is shared as `?q=`, and a category as `#ai` or `?cat=ai`.
- `docs/tools/` — one page per tool (overview, install, quick start, caveats, links)
- `docs/licenses.html` — Remotion, LTX-2, HunyuanVideo, WanGP, GPL, and code-versus-weights
- `docs/choose.html` — a decision table plus the job-by-job list
- `docs/notes.html` — data date, what was left out, and sources

Stars and last-push dates come from the GitHub API on 26 Oct 2026. They are not a live count.

## Browse locally

Open `docs/index.html` in a browser, or serve the folder:

```sh
python3 -m http.server 8765 --directory docs
```

Then visit `http://127.0.0.1:8765/`. Links are relative, so the folder works as a static site.

## Turn on GitHub Pages

1. Open this repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Choose branch **main** and folder **/docs**.
5. Save.

GitHub builds the site from the `docs` folder. `docs/.nojekyll` tells Pages to serve the HTML and CSS as-is, without running Jekyll. The first deployment can take a minute. After it finishes, the site is at:

https://sam4592.github.io/Animated-2026/

## Regenerating the HTML

`scripts/build_site.py` rewrites the pages in `docs/` from the catalog data in that script. Edit the data there, then run:

```sh
python3 scripts/build_site.py
```

Install commands in the script were checked against each project’s README or official install page on 26 Oct 2026. If a page could not show a verified command, it says so and links the repository or download page instead.
