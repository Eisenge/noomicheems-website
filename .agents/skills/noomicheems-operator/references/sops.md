# Noomicheems operations SOP — updated 2026-10-11

Standard operating procedures for operating Noomicheems (https://noomicheems.online/). These are the accumulated, verified workflows. Follow them in order; do not improvise around the verified steps.

## 0. Project baseline facts

- Production: https://noomicheems.online/ (Hostinger Business, account eisen.li@zoomex.com / hpanel user Shihchieh; site created 2026-10-08).
- Deployment source (the ONLY upload source, never /tmp/inc): local directory `noomicheems-deploy/` next to this repository's project folder.
- Languages: en (root) / ru / es / pt / id. Every page ships 6 hreflang (en/ru/es/pt/id + x-default), canonical, visible breadcrumb + BreadcrumbList JSON-LD. Hub pages also carry ItemList JSON-LD.
- Original game: https://jamesnorth.itch.io/noomiclone by jamesnorth. Embedded endpoint: https://itch.io/embed-upload/3164009.
- Owner's durable choices: Chinese communication, English site content, unofficial-site + original-game labeling, playable embedded homepage game (Play button, no external redirect), real pages behind every footer link, SEO-valid + 5-language for every new page, directory hub + breadcrumbs + sitemap for every new section.

## 1. Keyword → landing page SOP

1. Keyword sources: Web.Cafe https://new.web.cafe/data/updates and https://new.web.cafe/keywords?tab=evergreen&v=worth. Independently evaluate every candidate; verify intent with real Google searches (e.g. car driving → driving-school tutorials, watermark → encyclopedia, gpt chart → swallowed by ChatGPT). Never ask an AI to invent the keyword list.
2. Do not re-propose directions the owner rejected: reels/IG downloaders (AdSense risk), celebrity AI voices, windsurf-cam, AI baby/logo generators, new monetization tool sites ("先不建新站").
3. Fact-check with official sources (minecraft.net, news.xbox.com, news.blizzard.com, etc.) before writing copy; articles must cite official links.
4. Generate with the scripts in `noomicheems-deploy/`:
   - Landing pages: `build_i18n.py` (5-language dict + template).
   - News-section pages: `build_news.py` (news hub in 5 languages + article landing pages + footer links + sitemap regeneration). Run with `python3 build_news.py`.
5. Per-page SEO checklist (mandatory): unique title/h1/meta description, canonical, 6 hreflang, visible breadcrumb nav + BreadcrumbList JSON-LD (2 levels on hub, 3 on articles), ItemList JSON-LD on hubs, cross-links in footers (homepage ↔ games ↔ news).
6. Regenerate sitemap.xml in the same run (loc + lastmod). After upload, verify the live `<loc>` count matches expectations.

## 2. Deployment SOP (Hostinger File Manager)

1. Entry: https://hpanel.hostinger.com → Website Dashboard for noomicheems.online → "File manager / Edit your files" card → click the "Open" button. This opens File Browser in a new tab with a fresh token.
2. Direct URLs like https://srv1902-files.hstgr.io/<token>/files/public_html return 403 once the session expires — always re-enter through hpanel "Open".
3. Navigate to `/files/public_html` (site root).
4. New directory: "New folder" → type name into the prompt input (id `#focus-prompt`) → "Create".
5. Upload: click "Upload", choose the local file; when the "Replace all files in destination folder" dialog appears click the confirm button.
6. Hard lessons:
   - Long upload loops time out and silently skip files. Navigate per directory and upload per file, then verify with curl.
   - After editing app.js/i18n.js, BUMP the query version (e.g. `?v=20261012`) in every page that references them and re-upload those pages; otherwise browsers keep serving the cached old JS.
   - "Upload" succeeded / "Replace" clicked is NOT proof of deployment. Verify the live file afterwards (curl content or URL check).
   - File Browser's Vue inputs need real value setting + input event dispatch; use bu.js for the prompt input.

## 3. Online verification SOP

- HTTP status: `curl -s -o /dev/null -w "%{http_code}"` (site responds slowly; use python concurrent checks for batches).
- SEO markers: count `hreflang=` (expect 11 per page), `BreadcrumbList`, `ItemList`, canonical per page.
- Sitemap: count `<loc>` entries = expected URL count (currently 80).
- Game: browser click Play → within ~60 s status flips to the loaded copy; zero `ERR_BLOCKED_BY_RESPONSE` network entries.
- Use python `urllib` + `ThreadPoolExecutor` for batch checks; individual slow curl calls are unreliable in loops.

## 4. Game-outage SOP (itch.io)

Diagnosis chain (verify all before concluding):
1. Click Play on homepage → check `network_requests()` for `ERR_BLOCKED_BY_RESPONSE`.
2. `curl -sI https://itch.io/embed-upload/3164009`: `503` + `x-frame-options: SAMEORIGIN` means the platform endpoint is down/blocking embeds; `522` or `000` (timeout) means platform-level outage.
3. `curl` itch.io root / game page / API: `000` timeouts confirm platform-wide failure.
4. Public status: Downdetector, news of attacks/takedowns (Funko takedown, Cloudflare 521/522 host errors).

Fix (site side, already applied 2026-10-11):
- app.js fallback: iframe must fire `load` within 60 s; otherwise `showError()` renders a localized message + direct link https://jamesnorth.itch.io/noomiclone. i18n.js carries the `error` key in ru/es/pt/id.
- After changing app.js: bump version in all referencing pages, upload app.js + i18n.js + homepages, verify live.
- After itch.io recovers: re-check embed endpoint (200 and no SAMEORIGIN) → game auto-recovers; re-test Play in browser.
- If `embed-upload/3164009` is permanently dead after recovery, source a new embed URL from the game page and replace it in app.js.

## 5. GSC SOP

- Sitemap URL: https://noomicheems.online/sitemap.xml.
- Account: the owner's Hostinger/Google account (credentials are never stored in this repo). Google login requires user takeover (password page). Owner submits and reports; do not claim indexing without evidence.
- Status as of 2026-10-11: owner reported submitting the 80-URL sitemap.

## 6. Backlink SOP

- Consult references/backlinks.md BEFORE any submission to prevent duplicates; update the ledger after each verified outcome.
- Published so far: Medium, Dev.to, SoMuch (email confirmed), GamesNav (owner-reported contact), Curlie (suggestion received), GitHub repo. Guide drafts live in promotion/.
- A submitted form is not an approved backlink; only verified live listings count as evidence.

## 7. Keep-alive (screen saver)

- Long tasks on the owner's Mac: run `caffeinate -dims` in background to prevent screen sleep; check pid on resume.

## 8. Re-grounding pointers after context compression

- Read references/project-state.md, operations.md, backlinks.md.
- Live site is the source of truth; the local repo `public/` may lag production.
- Always deploy from `noomicheems-deploy/`, never /tmp/inc.
- Browser tabs/refs/tokens expire; re-observe before acting (see browser-use-automation-mac skill).
