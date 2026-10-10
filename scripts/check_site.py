from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import json,xml.etree.ElementTree as ET
P=Path(__file__).resolve().parents[1]/'public'
class Parse(HTMLParser):
 def __init__(self,s): super().__init__();self.tags=[];self.feed(s)
 def handle_starttag(self,t,a): self.tags.append((t,dict(a)))
urls=[n.text for n in ET.parse(P/'sitemap.xml').findall('.//{*}loc')]; assert len(urls)==len(set(urls))==40
for url in urls:
 path=urlsplit(url).path;f=P/path.lstrip('/')/'index.html';s=f.read_text();d=Parse(s);tags=d.tags
 assert sum(t=='h1' for t,a in tags)==1,f
 assert [a['href'] for t,a in tags if t=='link' and a.get('rel')=='canonical']==[url],f
 alts={a['hreflang']:a['href'] for t,a in tags if t=='link' and a.get('rel')=='alternate'}
 assert set(alts)=={'en','ru','es','pt','id','x-default'},f
 for alt in alts.values(): assert alt in urls,f
 for t,a in tags:
  href=a.get('href','') if t=='a' else a.get('src','')
  if href.startswith('/') and not href.startswith('//'):
   target=P/urlsplit(href).path.lstrip('/'); target=target/'index.html' if href.split('?')[0].split('#')[0].endswith('/') else target
   assert target.exists(),(f,href)
 for block in __import__('re').findall(r'<script type="application/ld\+json">(.*?)</script>',s): json.loads(block)
 assert 'noindex' not in s,f
 # Same page group must be reciprocal, not point all inner pages to home.
 for lang,alt in alts.items():
  other=Parse((P/urlsplit(alt).path.lstrip('/')/'index.html').read_text())
  other_alts={a['hreflang']:a['href'] for t,a in other.tags if t=='link' and a.get('rel')=='alternate'}
  assert other_alts==alts,(f,alt)
print('PASS: 40 pages; unique self-canonicals, reciprocal hreflang, JSON-LD, one H1 and all internal links/assets.')
