# Embedding an itch.io game in a static site: what I learned building a NoomiClone guide

*Published 2026-10-13 · by eisen · tags: webdev, gamedev, beginners, tutorial*

I built [noomicheems.online](https://noomicheems.online/), a static guide site for the browser game NoomiClone by [jamesnorth](https://jamesnorth.itch.io/noomiclone), with the game embedded on the homepage. It sounds trivial — drop an iframe in a static page — but there were three genuinely annoying problems. Here is what I learned, in case you are embedding any third-party game or app into your own site.

## The setup

The game is hosted on itch.io. The official embed endpoint is a plain iframe:

```html
<iframe src="https://itch.io/embed-upload/3164009" ...></iframe>
```

No API key, no SDK, no authentication. Just an iframe pointing at a URL that serves the game build.

## Problem 1: the embed refused to load (X-Frame-Options)

The first thing that surprised me: a `503` with `X-Frame-Options: SAMEORIGIN` on the embed endpoint. The game page itself was fine — the **embed endpoint** was the problem. This is a reminder that embed URLs are separate infrastructure from the game page; checking the game page is not enough.

**Lesson:** when you embed a third-party iframe, monitor the *embed URL*, not the marketing page. In practice the endpoint recovered within a day, but it convinced me the page needed a fallback.

## Problem 2: users stared at a blank box

During that outage, visitors saw an empty rectangle where the game should be. No error, no explanation. A blank box reads as "this site is broken" rather than "third-party service is down."

**Fix:** a load-time fallback. If the iframe has not fired its `load` event within 60 seconds, swap in a localized message ("the game host is having service issues") plus a direct link to the original game page. One small script, five lines of i18n keys, and the failure mode turns from "broken site" into "useful error."

## Problem 3: cross-origin means you cannot touch the game

Everything inside the iframe is cross-origin, so you cannot read its state, pause it, or add controls. You *can* wrap it — but the wrapper cannot know what is happening inside. Design for that:

- Keep keyboard controls documented *outside* the iframe (players focus the iframe first, then use keys).
- Give the iframe a generous fixed aspect ratio instead of forcing arbitrary sizes that crop the game.
- Never claim features you cannot verify (mobile controls, extra modes) just because the page would look more complete.

## What I would do differently

1. **Use a health check earlier.** A tiny cron that curls the embed URL every few minutes and flags status changes would have caught the outage minutes after it started.
2. **Test the fallback, not just the happy path.** I verified the game loads; I did not originally verify the 60-second fallback fires correctly. Test the failure path — it is the path users see during real incidents.
3. **Keep the original game clearly credited.** A guide or wrapper site has real value, but only if it is honest: independent site, original game, author credited, no fake features.

## Links

- The site: [noomicheems.online](https://noomicheems.online/)
- The original game: [NoomiClone by jamesnorth on itch.io](https://jamesnorth.itch.io/noomiclone)
- The project source (site + scripts): [github.com/Eisenge/noomicheems-website](https://github.com/Eisenge/noomicheems-website)

Embedding a third-party game is easy. Making that embed survive real-world incidents is the actual engineering. Hope this saves you the same afternoon I spent.
