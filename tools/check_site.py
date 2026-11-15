"""Prüft die vereinbarten lokalen Seiten und ihre Ressourcen."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1] / 'site'
HOSTS = {'www.if3t.de': 'main', 'sonnenstand-app.if3t.de': 'sonnenstand-app', 'sektoren-app.if3t.de': 'sektoren-app'}
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.h1 = 0
        self.ids = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'h1': self.h1 += 1
        if 'id' in a: self.ids.append(a['id'])
        for k in ['href', 'src']:
            if k in a: self.links.append(a[k])

pages = list(ROOT.rglob('*.html'))
assert len(pages) == 7, len(pages)
for file in pages:
    p = Page(); content = file.read_text(); p.feed(content)
    assert p.h1 == 1, file
    assert len(p.ids) == len(set(p.ids)), file
    assert '<html lang="de">' in content and 'rel="canonical"' in content, file
    area = file.relative_to(ROOT).parts[0]
    for link in p.links:
        u = urlsplit(link)
        if u.scheme == 'mailto': continue
        if u.netloc and u.netloc not in HOSTS: continue
        target_area = HOSTS.get(u.netloc, area)
        target = ROOT / target_area / (u.path.lstrip('/') or 'index.html')
        if not u.path: target = file
        assert target.is_file(), (file, link, target)
        if not u.netloc and u.fragment and target == file: assert u.fragment in p.ids, (file, link)
    if file.name != 'index.html': assert 'Arbeitsentwurf' in content and 'noindex, follow' in content, file
for asset in ['css/style.css', 'favicon.svg']:
    assert len({(ROOT / a / asset).read_bytes() for a in HOSTS.values()}) == 1, asset
print(f'OK: {len(pages)} Seiten, interne Links, lokale Ressourcen, Metadaten und Entwurfshinweise geprüft.')
