# Noomicheems website

Website source for [noomicheems.online](https://noomicheems.online/), an independent browser-play and guide site.

## Continue this project with an AI assistant

Start with [AGENTS.md](AGENTS.md) and the [Noomicheems operator skill](.agents/skills/noomicheems-operator/SKILL.md). The skill records owner decisions, project status, analytics troubleshooting and backlink submissions through 9 October 2026. It is a structured conversation handoff, not a verbatim transcript. Follow the latest user request and verify dated status before acting. Tools that do not automatically read repository instructions should be explicitly directed to these files.

The homepage embeds **NoomiClone, the original game by jamesnorth**. It is not the Noomicheems community mod and is not affiliated with or endorsed by the original creator.

## What is included

- A responsive embedded player with proportional scaling, reload and fullscreen controls.
- English controls, beginner guide, help, about, sources, privacy and terms pages.
- Page metadata, canonical URLs, structured data, sitemap and robots.txt.
- Optional Google Analytics with a visitor consent choice.
- Apache configuration for the production domain and a custom 404 page.

## Preview locally

No build step or package installation is required. With Python 3 installed, run from this repository:

```sh
python3 -m http.server 8765 --directory public
```

Open http://localhost:8765/. The embedded game requires an internet connection. The Python server does not apply Apache redirects or the custom 404 configuration.

## Deploy to Hostinger

Upload the **contents** of `public/`, including `.htaccess`, into the domain's `public_html/` directory. Preserve all subdirectories. README and other repository documentation do not belong in the web root.

This source is configured for `https://noomicheems.online/`. For a different deployment, review canonical URLs, sitemap, robots.txt, `.htaccess`, analytics configuration, ads.txt and policy text before publishing.

## Analytics and ads

`public/analytics.js` loads the configured Google Analytics tag only after a visitor chooses **Allow analytics**. It measures page views and site play/reload button clicks, not actions inside the third-party game. End-to-end reporting must be verified in the relevant Analytics property after deployment.

The measurement and publisher identifiers in these public files are website configuration, not account credentials. `ads.txt` does not by itself enable advertising or indicate AdSense approval.

## Game attribution and rights

- Original game: [NoomiClone by jamesnorth](https://jamesnorth.itch.io/noomiclone)
- Hosted embed: https://itch.io/embed-upload/3164009
- Site attribution: [Sources and credits](https://noomicheems.online/sources/)

This repository contains the site's HTML, CSS and JavaScript wrapper and guide pages. It does not contain the original game's source code, executable or game assets. Rights to the game remain with their respective owners; publishing this repository does not grant rights to redistribute or modify it. No software license is granted by this repository at present.

## Multilingual release — 10 October 2026

English remains at `/`; Russian, Spanish, Portuguese and Indonesian use `/ru/`, `/es/`, `/pt/` and `/id/`. Each locale has eight complete static pages, reciprocal HTML hreflang annotations, self-canonicals and matching language-switch links. The sitemap lists 40 canonical URLs. The embedded original game itself remains English.

Edit translations in `scripts/locales.json` and `scripts/more-locales.json`, then run `python3 scripts/build_locales.py`. English source remains in `public/`. Validate with `python3 scripts/check_site.py`. Shared player and analytics strings come from generated `public/i18n.js`. No browser-language redirects are used.

The player now uses a compact dark layout, a wide default view, optional fit-to-window mode and wrapper fullscreen with reload/exit controls. The complete original itch.io embed is retained, including attribution. Consent behavior remains opt-in; translating the UI does not add gameplay tracking.
