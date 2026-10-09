# Website and operations handoff

## Source and deployment

`public/` is the production document root. It contains index.html, app.js, analytics.js, style.css, favicon.svg, .htaccess, robots.txt, sitemap.xml, ads.txt, 404.html and the about, controls, guide, help, privacy, sources and terms directories.

Preview with `python3 -m http.server 8765 --directory public`. No package build is required. The Python server does not implement Apache redirects/custom error handling.

For an authorized Hostinger release, back up existing public files and upload the contents of public/ to the domain's public_html, preserving subdirectories and .htaccess. Keep .agents/, AGENTS.md and repository docs outside the web root. Verify HTTPS, homepage, affected pages and game after deployment. GitHub updates alone do not change production.

Earlier local work included separate public/, preview/, deploy/ and dated ZIP packages. preview/ was older; the latest documented package was noomicheems-ga4-upload.zip. Use current repository and live checks instead of guessing paths or choosing an old archive by name.

## Player and SEO invariants

- Homepage loads https://itch.io/embed-upload/3164009 after a Play action. It remains embedded in the page.
- Use full 1282 × 786 embed proportions, scaling the entire iframe. Fullscreen must fit both available dimensions. Avoid reintroducing cropped controls by forcing arbitrary iframe width/height.
- Itch.io attribution/toolbar stays visible. Third-party game canvas and controls are cross-origin; wrapper changes cannot alter internal UI.
- Keyboard controls: left arrow arch, Space tuck, up arrow release, R reset. Focus inside the iframe first. Do not invent mod features, mobile controls or maps.
- Preserve English copy, page-specific metadata/canonicals, JSON-LD, sitemap and working footer links. Canonical production origin is https://noomicheems.online/; .htaccess redirects HTTP/www to this origin.
- If changing player logic, inspect both app.js and any inline homepage script before editing; the current source may duplicate player initialization inline. Verify behavior, not just one file.

## GA4 unresolved diagnostic

Public measurement ID in source: G-L31XMH9HJH. Public AdSense publisher ID in ads.txt/meta: pub-1284741242592931. These are identifiers, not account credentials. Obtain private property access from the owner's current authenticated account, not from this skill.

analytics.js remembers the choice in localStorage key noomicheems_analytics. Before permission it defaults storage to denied and does not load the Google tag. “Allow analytics” loads it; “No thanks” leaves it unloaded. Footer Analytics settings lets the visitor change choice. Google signals and ad personalization are disabled. Events include pageviews, game_start_click and game_reload_click, not gameplay inside the iframe.

Prior verification established deployed code was present, but Google tag loading timed out in some local/browser attempts and GA4 realtime remained empty. Do not present network blocking as conclusively diagnosed or consent as necessarily the only cause.

When asked to fix no data:

1. Inspect the live HTML and analytics.js, expected ID and duplicate tags; compare with current repo, accounting for Hostinger/CDN caching.
2. Test both consent paths. Without changing the user's preference silently, use an isolated test session or their explicit choice to permit analytics.
3. Inspect whether the Google tag loads and actual collection requests are sent using supported developer/network tools, if available. Check browser blocking, network errors and console evidence. Do not use unauthorized page internals or hidden browser credentials.
4. Confirm the intended stream/property and relevant filters/debug/realtime evidence in GA4. If account permission is missing, ask for that specific access rather than modify code blindly.
5. Only change the demonstrated failure, then verify collection and reporting. Do not keep reuploading the same ZIP or call success solely because the script exists. Preserve accurate consent/privacy text.

## GSC and AdSense

Sitemap endpoint is /sitemap.xml. Submission was reported; indexing is unverified. AdSense review was last pending; ads.txt and account metadata are not proof of approval. Before adding live ads, verify approval and update privacy/consent behavior for the actual ad configuration. Do not state revenue estimates as earnings.

## Tool lessons from this project

GitHub connector authenticated as Eisenge and successfully wrote the full source via tree → commit → branch update. For future writes, fetch current head and preserve unrelated content; use a non-forced or expected-head update and recheck on conflict. An initial repo creation UI automatically applied the owner's existing Travis CI installation; no CI workflow was intentionally configured by this project.

Personal Chrome and in-app browser have independent sessions. Chrome extension control became unavailable; native app UI sometimes returned stale text or mismatched click outcomes. Verify visible current state after actions and avoid blind retries. Browser IDs and element indices in old conversations are not reusable instructions. Use current tool documentation and fresh page evidence.

For submissions or uploads, an attempted click is not completion. Look for a receipt, current repository contents or verified deployment. Keep passwords, cookies, authentication URLs, personal inbox content and unrelated machine state out of files and public commits.
