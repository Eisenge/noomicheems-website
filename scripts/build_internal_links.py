#!/usr/bin/env python3
# build_internal_links.py — insert "Related pages" nav (content pages) and "Explore more" section (homepages)
# into the noomicheems-deploy tree, 5 languages. Run from noomicheems-deploy/.
import os, re, html

LANGS = ["en", "ru", "es", "pt", "id"]
PREFIX = {"en": "", "ru": "/ru", "es": "/es", "pt": "/pt", "id": "/id"}

# slug -> list of related slugs (relative to language root)
RELATED = {
    "guide": ["controls", "noomiclone-tips", "help"],
    "controls": ["guide", "noomiclone-tips", "help"],
    "help": ["guide", "controls", "noomiclone-tips"],
    "noomiclone-tips": ["guide", "controls", "games"],
    "freeze-tag-meaning": ["noomiclone-tips", "games", "news"],
    "halo-ce-browser": ["lagos-life-game", "noomiclone-tips", "games"],
    "lagos-life-game": ["halo-ce-browser", "noomiclone-tips", "games"],
    "the-sift-minecraft": ["wow-forever", "news", "games"],
    "wow-forever": ["the-sift-minecraft", "news", "games"],
    "games": ["news", "noomiclone-tips", "freeze-tag-meaning"],
    "news": ["the-sift-minecraft", "wow-forever", "games"],
}
EXPLORE = ["guide", "controls", "noomiclone-tips", "news", "games"]

LABEL_REL = {
    "en": "Related pages", "ru": "Похожие страницы", "es": "Páginas relacionadas",
    "pt": "Páginas relacionadas", "id": "Halaman terkait",
}
LABEL_EXP = {
    "en": "Explore more", "ru": "Смотреть ещё", "es": "Explorar más",
    "pt": "Explorar mais", "id": "Jelajahi lainnya",
}

def get_anchor(path):
    """Extract a clean anchor text from the page's <h1> (fallback: <title>)."""
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return None
    m = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.S)
    if m:
        t = re.sub(r"<[^>]+>", "", m.group(1))
        return html.unescape(t).strip()
    m = re.search(r"<title>(.*?)</title>", content, re.S)
    if m:
        t = m.group(1)
        t = re.sub(r"\s*[|–-]\s*Noomicheems.*$", "", t)
        return html.unescape(t).strip()
    return None

def page_path(lang, slug):
    if lang == "en":
        return os.path.join("index.html" if slug == "index" else slug, "index.html")
    return os.path.join(lang, slug, "index.html")

# Preload anchors per (lang, slug)
anchors = {}
for lang in LANGS:
    for slug in set(list(RELATED) + EXPLORE + ["index"]):
        p = page_path(lang, slug)
        if os.path.exists(p):
            anchors[(lang, slug)] = get_anchor(p)

missing = [(l, s) for (l, s) in anchors if anchors[(l, s)] is None]
if missing:
    print("MISSING anchors:", missing)

def url(lang, slug):
    if slug == "index":
        return PREFIX[lang] + "/" if lang != "en" else "/"
    return PREFIX[lang] + "/" + slug + "/"

def build_related_block(lang, slug):
    parts = [f'<nav class="related" aria-label="{html.escape(LABEL_REL[lang])}"><h2 class="related-title">{LABEL_REL[lang]}</h2>']
    for r in RELATED[slug]:
        a = anchors.get((lang, r))
        if not a:
            continue
        parts.append(f'<a href="{url(lang, r)}">{html.escape(a)}</a>')
    parts.append("</nav>")
    return "".join(parts)

def build_explore_block(lang):
    parts = [f'<section class="explore" aria-label="{html.escape(LABEL_EXP[lang])}"><h2 class="explore-title">{LABEL_EXP[lang]}</h2>']
    for r in EXPLORE:
        a = anchors.get((lang, r))
        if not a:
            continue
        parts.append(f'<a href="{url(lang, r)}">{html.escape(a)}</a>')
    parts.append("</section>")
    return "".join(parts)

count = 0
# 1) Content pages: insert Related nav before </main>
for lang in LANGS:
    for slug in RELATED:
        p = page_path(lang, slug)
        if not os.path.exists(p):
            print("SKIP (no file):", p)
            continue
        with open(p, encoding="utf-8") as f:
            c = f.read()
        if 'class="related"' in c:
            continue
        block = build_related_block(lang, slug)
        if not block or '<a href=' not in block:
            print("SKIP (no anchors):", p)
            continue
        c2 = c.replace("</main>", block + "</main>", 1)
        if c2 == c:
            print("NO INSERT POINT:", p)
            continue
        with open(p, "w", encoding="utf-8") as f:
            f.write(c2)
        count += 1

# 2) Homepages: insert Explore section before </main>
for lang in LANGS:
    p = page_path(lang, "index")
    if not os.path.exists(p):
        print("SKIP (no file):", p)
        continue
    with open(p, encoding="utf-8") as f:
        c = f.read()
    if 'class="explore"' in c:
        continue
    block = build_explore_block(lang)
    if not block or '<a href=' not in block:
        print("SKIP (no anchors):", p)
        continue
    c2 = c.replace("</main>", block + "</main>", 1)
    if c2 == c:
        print("NO INSERT POINT:", p)
        continue
    with open(p, "w", encoding="utf-8") as f:
        f.write(c2)
    count += 1

print("Inserted blocks:", count)
