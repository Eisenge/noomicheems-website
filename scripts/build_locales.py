"""Generate translated static pages and reciprocal language links. English stays editable in public/."""
import json,re,html
from pathlib import Path
from xml.etree.ElementTree import Element,SubElement,ElementTree
ROOT=Path(__file__).resolve().parents[1]; PUB=ROOT/'public'; ORIGIN='https://noomicheems.online'
D=json.loads((ROOT/'scripts/locales.json').read_text()); D.update(json.loads((ROOT/'scripts/more-locales.json').read_text()))
LANGS={'en':'English','ru':'Русский','es':'Español','pt':'Português','id':'Bahasa Indonesia'}
PAGES=['','controls','guide','about','sources','privacy','terms','help']
def path(lang,page=''): return '/' + (lang+'/' if lang!='en' else '') + (page+'/' if page else '')
def esc(s): return html.escape(s,quote=True)
def alternates(page): return ''.join(f'<link rel="alternate" hreflang="{l}" href="{ORIGIN}{path(l,page)}">' for l in LANGS)+f'<link rel="alternate" hreflang="x-default" href="{ORIGIN}{path("en",page)}">'
def languages(lang,page):
    label=D[lang]['language'] if lang in D else 'Language'
    return '<nav class="languages" aria-label="'+label+'">'+''.join(f'<a href="{path(l,page)}" lang="{l}" hreflang="{l}"'+(' aria-current="page"' if l==lang else '')+f'>{name}</a>' for l,name in LANGS.items())+'</nav>'
for page in PAGES:
    file=PUB/(page+'/index.html' if page else 'index.html'); s=file.read_text()
    s=re.sub(r'<link rel="alternate"[^>]*>','',s)
    s=re.sub(r'<nav class="languages".*?</nav>','',s)
    s=s.replace('</head>',alternates(page)+'</head>').replace('</header>','</header>'+languages('en',page))
    s=s.replace('/analytics.js"','/analytics.js?v=20261010"')
    s=s.replace('before analytics or advertising is introduced','before advertising is introduced')
    s=s.replace('including the optional third-party itch.io card.','including the embedded itch.io game and optional Google Analytics.')
    s=s.replace('The site’s illustrations are original explanatory artwork, not screenshots or representations of an available mod.','The game shown in the player is the original browser release, not a representation of an available mod.')
    file.write_text(s)
for lang,d in D.items():
  for page in PAGES:
    title=d['title'] if not page else d['pages'][page][0]+' | Noomicheems'
    desc=d['desc'] if not page else d['pages'][page][1]
    url=ORIGIN+path(lang,page); n=d['nav']
    schema={'@context':'https://schema.org','@type':'WebPage','name':title,'url':url,'description':desc,'inLanguage':lang,'isPartOf':{'@type':'WebSite','name':'Noomicheems','url':ORIGIN+'/'}}
    head=f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow"><title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><meta name="theme-color" content="#171a1b"><link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="/style.css?v=20261010"><link rel="canonical" href="{url}">{alternates(page)}<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script><meta name="google-adsense-account" content="ca-pub-1284741242592931"><script src="/i18n.js?v=20261010" defer></script><script src="/analytics.js?v=20261010" defer></script><script src="/app.js?v=20261010" defer></script></head>'
    header=f'<body><a class="skip" href="#main">{d["skip"]}</a><header><a class="brand" href="/{lang}/">n<span>↗</span> <b>noomicheems</b></a><nav aria-label="{d["language"]}"><a href="/{lang}/#game">{n[0]}</a><a href="/{lang}/controls/">{n[1]}</a><a href="/{lang}/guide/">{n[2]}</a></nav><a class="small" href="/{lang}/about/">{d["independent"]} ↗</a></header>'+languages(lang,page)
    foot=f'<footer><a class="brand" href="/{lang}/">noomicheems<span>↗</span></a><p>{d["credit"]}</p><nav aria-label="{d["independent"]}">'+''.join(f'<a href="/{lang}/{p}/">{n[idx]}</a>' for p,idx in [('about',3),('controls',1),('guide',2),('sources',4),('privacy',5),('terms',6),('help',7)])+'</nav></footer></body></html>'
    if not page:
      a=d['actions']
      body=f'<main id="main"><section class="playhead"><div><p class="eyebrow">NOOMICHEEMS.ONLINE / {d["original"]}</p><h1>{d["headline"]}</h1><p>{d["intro"]}</p></div></section><div id="play-shell"><section class="player" id="game" aria-label="{d["original"]}"><div id="game-start" class="game-start"><h2>{d["original"]}</h2><p>{d["intro"]}</p><button id="start-game" class="button" type="button">{d["play"]}</button><p class="fine">{d["wait"]}</p></div></section><div class="playbar"><span><b>←</b> {a[0]} &nbsp; <b>Space</b> {a[1]} &nbsp; <b>↑</b> {a[2]} &nbsp; <b>R</b> {a[3]}</span><div><button id="view-game" type="button" aria-pressed="true">{d["fit"]}</button><button id="reload-game" type="button">{d["reload"]}</button><button id="fullscreen-game" type="button">{d["full"]}</button></div></div></div><p class="fine" id="game-status" role="status">{d["ready"]}</p><p class="fine player-note">{d["credit"]} <a href="/{lang}/help/">{n[7]}</a></p><p class="fine">{d["gameLanguage"]}</p><section class="game-intro"><h2>{d["what"]}</h2><p>{d["whatText"]}</p><p>{d["modText"]} <a href="/{lang}/sources/">{n[4]} →</a></p></section><section><div class="sectionhead"><h2>{d["basics"]}</h2><a href="/{lang}/controls/">{n[1]} →</a></div><div class="keys">'+''.join(f'<article><kbd>{key}</kbd><h3>{action}</h3></article>' for key,action in zip(['←','SPACE','↑','R'],a))+f'</div></section><section class="split"><div><h2>{d["faq"]}</h2><a href="/{lang}/guide/">{n[2]} →</a></div><div>'+''.join(f'<details><summary>{q}</summary><p>{ans}</p></details>' for q,ans in d['questions'])+'</div></section></main>'
    else:
      h,desc,sections=d['pages'][page]
      body=f'<main id="main"><article class="article"><p class="eyebrow">NOOMICHEEMS.ONLINE</p><h1>{h}</h1><p class="intro">{desc}</p>'+''.join(f'<h2>{heading}</h2><p>{text}</p>' for heading,text in sections)
      if page in ['sources','about','controls']:
        body+='<p><a href="https://jamesnorth.itch.io/noomiclone">NoomiClone — jamesnorth / itch.io ↗</a></p>'
      if page=='privacy':
        body+='<p><a href="https://itch.io/docs/legal/privacy-policy">itch.io — '+n[5]+'</a> · <a href="https://policies.google.com/privacy">Google — '+n[5]+'</a></p>'
      body+=f'<p><a class="button" href="/{lang}/#game">{n[0]} →</a> <a href="/{lang}/help/">{n[7]}</a></p></article></main>'
    dest=PUB/path(lang,page).lstrip('/')/'index.html'; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_text(head+header+body+foot)
# Static URLs remain usable without JavaScript. Client strings only affect controls and consent.
client={l:{k:v for k,v in d.items() if k in ['fit','expand','full','exit','loading','loaded','slow','noFull','consent']} for l,d in D.items()}
(PUB/'i18n.js').write_text('window.noomiLocale = '+json.dumps(client,ensure_ascii=False)+'[document.documentElement.lang] || {};\n')
root=Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
for lang in LANGS:
 for page in PAGES:
  u=SubElement(root,'url'); SubElement(u,'loc').text=ORIGIN+path(lang,page); SubElement(u,'lastmod').text='2026-10-10'
ElementTree(root).write(PUB/'sitemap.xml',encoding='utf-8',xml_declaration=True)
print('Generated 32 translations, enhanced 8 English pages; sitemap contains 40 URLs.')
