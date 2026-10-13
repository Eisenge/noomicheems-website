#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inject a visible breadcrumb + 3-level BreadcrumbList JSON-LD into the 4
hand-written English pages so they match the script-generated pages."""
import os, re, json

DEPLOY = os.path.dirname(os.path.abspath(__file__))
SITE = "https://noomicheems.online"
SHORT = {
    "lagos-life-game": "Lagos Life Game",
    "halo-ce-browser": "Halo CE Browser",
    "freeze-tag-meaning": "Freeze Tag",
    "noomiclone-tips": "NoomiClone Tips",
}
OLD2 = re.compile(
    r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": \[\{"@type": "ListItem", "position": 1, "name": "Noomicheems", "item": "https://noomicheems\.online/"\}, \{"@type": "ListItem", "position": 2, "name": "[^"]*", "item": "https://noomicheems\.online/(?:[a-z-]+/)?[a-z-]+/"\}\]\}</script>'
)
CRUMB = ('<nav class="breadcrumbs" aria-label="Breadcrumb">'
         '<a href="/">Home</a><span aria-hidden="true">›</span>'
         '<a href="/games/">Browser Games</a><span aria-hidden="true">›</span>'
         '<span aria-current="page">{short}</span></nav>')

for slug, short in SHORT.items():
    p = os.path.join(DEPLOY, slug, "index.html")
    with open(p, encoding="utf-8") as f:
        html = f.read()
    # 1. Replace the 2-level BreadcrumbList with a 3-level one.
    new_ld = ('<script type="application/ld+json">{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ['
              '{"@type": "ListItem", "position": 1, "name": "Noomicheems", "item": "https://noomicheems.online/"}, '
              '{"@type": "ListItem", "position": 2, "name": "Browser Games", "item": "https://noomicheems.online/games/"}, '
              '{"@type": "ListItem", "position": 3, "name": "' + short + '", "item": "https://noomicheems.online/' + slug + '/"}]}</script>')
    n_html, n = OLD2.subn(new_ld, html)
    assert n == 1, (slug, "ld", n)
    # 2. Insert the visible breadcrumb right after <main id="main">.
    needle = '<main id="main"><article class="article">'
    assert needle in n_html, (slug, "main")
    n_html = n_html.replace(needle, '<main id="main">' + CRUMB.format(short=short) + '<article class="article">', 1)
    with open(p, "w", encoding="utf-8") as f:
        f.write(n_html)
    print("patched", slug)
