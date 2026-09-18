#!/usr/bin/env python3
"""Inline the processed data into the page template and write the standalone site.

Run `python build/prep.py` first (it rebuilds data/disapprovals.json from the
source workbook), then `python build/build.py`.

The output is a single self-contained index.html: no external scripts, no tile
server, no build step at serve time. The only outbound request is the Google
Fonts stylesheet, and the page falls back to Georgia and a system sans if that
is blocked.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL  = os.path.join(ROOT, 'build', 'template.html')
DATA = os.path.join(ROOT, 'data', 'disapprovals.json')
OUT  = os.path.join(ROOT, 'index.html')

tpl = open(TPL, encoding='utf-8').read()

# Leaflet's stylesheet is inlined: artifact pages only admit external
# stylesheets from Google Fonts, so the library CSS has to ship in the page.
CSS = os.path.join(ROOT, 'build', 'vendor', 'leaflet-1.9.4.css')
tpl = tpl.replace('__LEAFLET_CSS__', open(CSS, encoding='utf-8').read().strip())
payload = open(DATA, encoding='utf-8').read()

# Simplified park outlines, keyed by unit code. Regenerated only by
# build/fetch_boundaries.py, which is the one script here that touches the
# network; this build stays offline.
BOUND = os.path.join(ROOT, 'build', 'vendor', 'nps-boundaries.json')
boundaries = open(BOUND, encoding='utf-8').read().strip()


def guard(text):
    """Keep the JSON from closing the <script> element or tripping older parsers."""
    return (text.replace('<', '\\u003c')
                .replace('\u2028', '\\u2028')
                .replace('\u2029', '\\u2029'))


html = tpl.replace('__PAYLOAD__', guard(payload)).replace('__BOUNDARIES__', guard(boundaries))
open(OUT, 'w', encoding='utf-8').write(html)

d = json.loads(open(DATA, encoding='utf-8').read())
print('wrote', OUT)
print('  %d KB' % (len(html.encode('utf-8')) // 1024))
print('  %d agreements, %d locations' % (len(d['recs']), len(d['units'])))
