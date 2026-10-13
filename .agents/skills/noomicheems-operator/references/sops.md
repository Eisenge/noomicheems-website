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
4. Generate with the scripts in this repo's `scripts/` (copied from the deploy source; run them from a working copy of the site tree):
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

## 11. Internal-links SOP (added 2026-10-13)

Purpose: strengthen site-internal linking — "Related pages" nav on every content page and an "Explore more" section on every homepage, 5 languages, to distribute link equity and help crawlers discover deep pages.

1. Script: `scripts/build_internal_links.py` in this repo (run from a working copy of the site tree, `python3 build_internal_links.py`). It reads the RELATED slug map (guide/controls/help/noomiclone-tips/freeze-tag-meaning/halo-ce-browser/lagos-life-game/the-sift-minecraft/wow-forever/games/news) and EXPLORE list (guide/controls/noomiclone-tips/news/games).
2. Anchor text: extracted from each target page's `<title>` (descriptive), stripping trailing `—/| Noomicheems` suffixes; h1 fallback. Labels localized per language (Related pages / Похожие страницы / Páginas relacionadas / Halaman terkait; Explore more / Смотреть ещё / Explorar más / Jelajahi lainnya).
3. Insertion point: immediately before `</main>` on each page (55 content pages + 5 homepages = 60 blocks).
4. Styles: append `.related,.explore` block styles to `style.css` (pill links on dark theme). After appending CSS, RE-UPLOAD style.css and verify the live file contains the new rules (curl) — the first upload attempt silently failed (Replace dialog handled twice); always verify.
5. Deployment: upload per directory via File Browser (61 files: root index.html + style.css, 11 content dirs × 5 languages incl. each language root index.html). Upload loops time out — split by language, re-enter token via hpanel "Open" if 403, use `bu.wait_for_element("#upload-input")` before each upload, and confirm the "Replace all files" modal via JS click.
6. Verify live with parallel python urllib checks: `.related`/`.explore` blocks and link counts per URL; expect related=1 or explore=1. Slow CDN cold-cache responses on some paths are transient; re-check rather than concluding failure.

## 8. Re-grounding pointers after context compression (updated 2026-10-13)

- Read references/project-state.md, operations.md, backlinks.md.
- Live site is the source of truth; the local repo `public/` may lag production.
- Always deploy from `noomicheems-deploy/`, never /tmp/inc.
- Browser tabs/refs/tokens expire; re-observe before acting (see browser-use-automation-mac skill).

## 9. Daily keyword screening SOP (cross-site, owner-approved 2026-10-13)

Purpose: every day, scan Web.Cafe for new keywords, judge what can be built (page vs new site), and log the decision. This is the pipeline feeding new pages/sites across all owner sites.

### 9.1 Daily data sources (about 10 min, once per day)
1. Updates feed: https://new.web.cafe/data/updates — daily batches (new words / resurgence / mini-games). The "recently scanned" line shows today's batches.
2. Resurgence board: https://new.web.cafe/keywords?tab=resurgence — filter "值得做" (worth doing). GPTs multiple = 7-day heat ÷ GPTs heat.
3. Evergreen board: https://new.web.cafe/keywords?tab=evergreen&v=worth — long-tail stable words, worth-checking filter.

### 9.2 Screening criteria (apply in order; a candidate passes only if all relevant checks pass)
1. Volume: GPTs × ≥ 0.05 = standalone-site line; × 0.01–0.05 = inner-page candidate; below = skip unless long-tail family is large.
2. Trend: rising (+%) preferred; "回落中" (declining) = skip; check the peak date vs today — a spike older than ~5 days with no sustained rise is a short-lived news spike.
3. Competition: read "谷歌前两页" section — no dedicated homepage / mostly big-site inner pages = opportunity; a new-site homepage already ranking top 5 = inner page or skip; check first-page intent by real Google search (owner rule: remove ambiguous keywords).
4. Intent: one clear intent, no brand-name collision or multi-game/multi-product mixing; verify with an actual Google SERP before building.
5. Fit with existing sites: fits noomicheems (browser games / game news) or krillion (krillion-related) or a tool site → prefer inner page/news page in existing site; genuinely new theme → candidate new site.
6. Rejected directions (never re-propose): reels/IG/YouTube downloaders, celebrity AI voice, AI baby/logo generators, windsurf-cam, new monetization tool sites (owner said "先不建新站" during the noomicheems phase).

### 9.3 Decision output (log every day to a ledger)
- 值得做 → note: inner page / news page (run build_i18n.py / build_news.py, 5 languages) or new site (draft: main keyword + domain + business model).
- 可以试试 → re-check in 2–3 days before acting.
- 不值得做 → archive with reason.

### 9.4 Execution rhythm
- Daily: scan the 3 sources → shortlist 5–10 candidates → update ledger.
- Weekly: ship 1–3 best candidates (inner page / news page / new site).
- Re-scan the ledger before any submission/deployment to avoid duplicates.

## 10. Post-launch operations SOP (applies to noomicheems and any new site)

Verified from Web.Cafe methodology (owner's learning requirement 2026-10-13):

### 10.1 Launch day
- GSC: submit domain property + sitemap (https://<domain>/sitemap.xml).
- GA4: tag deployed and verified (real events arriving).
- robots.txt: explicitly allow AI crawlers — GPTBot, Claude-Web, Anthropic-AI, PerplexityBot, Google-Extended, OAI-SearchBot, CCBot; point to llms.txt / llms-full.txt.
- llms.txt + llms-full.txt present (SagaSu case: 12.5万 AI crawls observed).
- Self-check canonical / hreflang / breadcrumbs / JSON-LD on every page.

### 10.2 Week 1
- Content rhythm: add ≥1 page every 1–2 days (keyword pages or news), all languages of the site.
- GSC: request indexing for each new URL after deploy.
- Backlinks batch 1: GitHub repo README, Medium guide, Dev.to guide, relevant directories (check backlinks.md ledger first).
- Internal links: every new page reachable from a hub + breadcrumbs (owner rule).

### 10.3 Month 1
- Keep content cadence; 1 backlink every 2–3 days from varied sources.
- GEO: titles include the year for AI search-crawler matching (e.g. "… 2026"); strong/absolute phrasing where factual.
- Watch GSC: indexed count, impressions trend, keyword rank movement (target top 20).
- Watch GA4: pageviews, engagement; for monetized pages track conversion events (register/subscribe).

### 10.4 Viability check (4–6 weeks)
- Signals of life: indexing grows, impressions appear, some keywords reach top 20, repeat visitors.
- No indexing / no impressions → check robots.txt, quality (thin/AI-template pages), duplicate content, sitemap submission.
- Decide: keep investing, pivot keywords, or park the site. Do not state traffic numbers that were not verified.

