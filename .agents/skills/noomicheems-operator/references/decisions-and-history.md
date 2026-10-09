# Decisions and conversation history

This ordered summary preserves changes in scope. It is not a verbatim transcript. Dates are only supplied where known.

## 1. Business and keyword selection

The owner initially wanted a subscription service website and asked for SEO keyword research before construction. They selected the English overseas market and a monthly operating/tools budget of RMB 500–2000. This is planning context, not permission to spend.

They supplied https://new.web.cafe/chat and clarified that it teaches methods: learn those methods and independently find keywords, rather than directly asking its AI which keywords to use. They then asked to choose from https://new.web.cafe/data/updates . Do not invent keyword volumes or difficulty scores that are not in retained evidence.

The owner broadened the model to high-traffic mini-game keywords with advertising monetization, referencing https://new.web.cafe/tutorial/detail/65tv6y1tzb . They chose Noomicheems. This superseded the subscription idea for this particular site.

They asked about revenue for 400,000 monthly UV using https://new.web.cafe/tutorial/detail/ixsok5mmfm . No reliable prior numeric conclusion is retained here. If revisited, read the source and model UV → sessions/pageviews → monetized impressions → revenue with explicit geography, fill and RPM assumptions; never treat UV as ad impressions.

## 2. Build, domain and game selection

The owner first requested a preview before buying a domain, then purchased noomicheems.online in Hostinger and reported hosting purchased. They authorized working through their GitHub/Hostinger accounts for the site; current login still needs verification when used.

The homepage must feature the game itself so visitors can play without leaving the site. The owner approved using NoomiClone original, clearly labeled, when only community APK clues were available for Noomicheems. They had no playable link and asked the assistant to find it.

The implementation uses the developer-published itch.io browser embed. It must not pretend to be a community mod, official publisher or owner of the game. The game binary/assets are not in the source repository.

They requested SEO on the homepage and a real page for every footer link, followed by domain deployment. A screenshot later highlighted oversized/cropped side controls. The website wrapper was changed to scale the entire fixed-size embed rather than crop it. Original game UI elements remain controlled by the third-party build.

## 3. Search, ads and analytics

Owner requested GSC, AdSense and GA4 setup. They manually assisted with DNS and uploads when browser control failed. GSC sitemap submission was reported done; AdSense site entry and verification were prepared, last known review pending.

GA4 repeatedly showed no data. The owner asked to recheck code and reupload. Prior work found deployed analytics code matching the local package but did not establish successful collection; repeated identical uploads did not prove a fix. Browser network access to Google tag resources timed out in some attempts. Preserve this uncertainty.

## 4. Other keyword ideas

Owner asked to inspect the newer table https://new.web.cafe/data/updates/2026-10-08T0540 and asked what “norges dummeste quiz” means. No complete scored shortlist from that analysis is retained.

Owner proposed “ductworks roblox” and selected preview before purchasing a domain. Keep this a separate project. Do not claim its implementation or publication is complete without locating evidence.

## 5. Backlink acquisition

Owner asked to follow the Web Cafe discussion https://new.web.cafe/topic/yaylfflusn and allowed questions to its AI. Prior reading attributed the post to community author 飞天, not to 哥飞 personally. Retained method: inspect relevant competitors' backlinks, filter quality, check submission rules manually, test one or two opportunities, record outcomes. An authority-score reference was ambiguous; do not turn “90” into a rigid requirement.

Owner asked to use Semrush. Login was reached but blocked by an active-session limit. Terminating another session was not authorized. No Semrush backlink export or authority scores were obtained, so do not describe this candidate list as Semrush-verified.

GamesNav, Curlie, the GitHub project and SoMuch were progressed one at a time; see backlinks.md. Owner explicitly authorized sending the GamesNav message. Subsequent confirmations were specific to their own forms and do not grant blanket outreach permission.

## 6. Source publishing and current handoff

On 2026-10-09 the owner asked to upload the actual project to GitHub and completed login as Eisenge. Repository noomicheems-website was created publicly, source uploaded, README included a live website link and game attribution, and public readability verified. Hostinger production was not automatically connected to GitHub.

After reporting SoMuch submitted, the owner requested this skill to preserve the dialogue for future AI work. It provides actionable continuity, explicitly separates evidence levels, and excludes personal and unrelated browser data from the public repo.
