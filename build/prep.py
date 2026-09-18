import openpyxl, json, re, html

import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC    = os.path.join(ROOT, 'data', 'source', 'verified-disapprovals-with-abstract-and-impact.xlsx')
OUT    = os.path.join(ROOT, 'data', 'disapprovals.json')

# Park unit codes. Everything else in the data is an office, a national
# program, or a monitoring network, which the map draws as a square.
PARKS = {
    'ARCH', 'AZRU', 'BELA', 'BOHA', 'BRCA', 'CACO', 'CARE', 'CHIC', 'CRMO',
    'DENA', 'DEVA', 'EFMO', 'FLFO', 'GATE', 'GLAC', 'GLCA', 'GOGA', 'GRSA',
    'HALE', 'HAVO', 'JODA', 'JOTR', 'LAKE', 'LARO', 'LYJO', 'MALU', 'MANZ',
    'MEMY', 'MIMA', 'MOJA', 'MORA', 'NERI', 'ORCA', 'ORPI', 'PETR', 'PORE',
    'PUHO', 'REDW', 'SEKI', 'TUAI', 'TUSK', 'VALL', 'WACO', 'WHIS', 'YELL',
    'YOSE', 'ZION',
}

# Official unit names from the same NPS service.
NAMES = {
"GLAC":"Glacier National Park","REDW":"Redwood National Park","MEMY":"Medgar and Myrlie Evers Home National Monument",
"BOHA":"Boston Harbor Islands National Recreation Area","FLFO":"Florissant Fossil Beds National Monument",
"LARO":"Lake Roosevelt National Recreation Area","GRSA":"Great Sand Dunes National Park and Preserve",
"HAVO":"Hawai'i Volcanoes National Park","WACO":"Waco Mammoth National Monument","PETR":"Petroglyph National Monument",
"JOTR":"Joshua Tree National Park","MIMA":"Minute Man National Historical Park","LYJO":"Lyndon B. Johnson National Historical Park",
"ORPI":"Organ Pipe Cactus National Monument","MALU":"Martin Luther King, Jr., National Historical Park",
"BRCA":"Bryce Canyon National Park","WHIS":"Whiskeytown-Shasta-Trinity National Recreation Area",
"PORE":"Point Reyes National Seashore","TUSK":"Tule Springs Fossil Beds National Monument","YOSE":"Yosemite National Park",
"DEVA":"Death Valley National Park","CACO":"Cape Cod National Seashore","GATE":"Gateway National Recreation Area",
"VALL":"Valles Caldera National Preserve","GLCA":"Glen Canyon National Recreation Area","TUAI":"Tuskegee Airmen National Historic Site",
"NERI":"New River Gorge National Park and Preserve","PUHO":"Pu'uhonua o Honaunau National Historical Park",
"CHIC":"Chickasaw National Recreation Area","CRMO":"Craters of the Moon National Monument and Preserve",
"CARE":"Capitol Reef National Park","LAKE":"Lake Mead National Recreation Area","MORA":"Mount Rainier National Park",
"AZRU":"Aztec Ruins National Monument","MANZ":"Manzanar National Historic Site","ZION":"Zion National Park",
"JODA":"John Day Fossil Beds National Monument","GOGA":"Golden Gate National Recreation Area",
"EFMO":"Effigy Mounds National Monument","HALE":"Haleakala National Park","ARCH":"Arches National Park",
"BELA":"Bering Land Bridge National Preserve","YELL":"Yellowstone National Park","MOJA":"Mojave National Preserve",
"DENA":"Denali National Park and Preserve","ORCA":"Oregon Caves National Monument and Preserve",
"SEKI":"Sequoia and Kings Canyon National Parks",
# Offices, programs and monitoring networks: no single park boundary, so they sit off the map.
"AKRO":"Alaska Regional Office","IMRO":"Intermountain Regional Office","NERO":"Northeast Regional Office",
"PWRO":"Pacific West Regional Office","WASO":"Washington Support Office (NPS headquarters)",
"MWAC":"Midwest Archeological Center","NRSS":"Natural Resource Stewardship and Science directorate",
"HPTC":"Historic Preservation Training Center","RTCA":"Rivers, Trails, and Conservation Assistance program",
"NTIR":"National Trails Office, Intermountain Region","CRAD":"Cultural Resources Directorate",
"CHBA":"Chesapeake Bay Office / Chesapeake Gateways Network","JUBA":"Juan Bautista de Anza National Historic Trail",
"KLMN":"Klamath Inventory and Monitoring Network","MOJN":"Mojave Desert Inventory and Monitoring Network",
"SIEN":"Sierra Nevada Inventory and Monitoring Network","SWAN":"Southwest Alaska Inventory and Monitoring Network",
}


PLACE = {
 "WASO":"NPS headquarters, Washington, DC","CRAD":"NPS headquarters, Washington, DC",
 "RTCA":"NPS headquarters, Washington, DC","NRSS":"NPS headquarters, Washington, DC",
 "AKRO":"Anchorage, Alaska","SWAN":"Anchorage, Alaska","IMRO":"Lakewood, Colorado",
 "NERO":"Philadelphia, Pennsylvania","PWRO":"San Francisco, California","JUBA":"Richmond, California",
 "MWAC":"Lincoln, Nebraska","HPTC":"Frederick, Maryland","NTIR":"Santa Fe, New Mexico",
 "CHBA":"Annapolis, Maryland","KLMN":"Ashland, Oregon","MOJN":"Boulder City, Nevada",
 "SIEN":"Three Rivers, California",
}

# Geographic coordinates behind the projected positions above, kept so the published
# CSV carries real lat/lon. Parks: NPS boundary centroids. Offices: the published
# office address, geocoded. See docs/PLACEMENTS.md.
LATLON = {
"GLAC":[48.6189,-113.7563],"REDW":[41.2776,-124.0045],"MEMY":[32.3408,-90.2138],"BOHA":[42.2621,-70.8758],
"FLFO":[38.9126,-105.2860],"LARO":[47.9106,-118.3510],"GRSA":[37.7669,-105.6130],"HAVO":[19.3031,-155.2395],
"WACO":[31.6049,-97.1762],"PETR":[35.1400,-106.7453],"JOTR":[33.8993,-115.9533],"MIMA":[42.4549,-71.2999],
"LYJO":[30.2516,-98.6251],"ORPI":[32.0084,-112.8755],"MALU":[33.7549,-84.3717],"BRCA":[37.5708,-112.1856],
"WHIS":[40.6163,-122.6127],"PORE":[38.0708,-122.9175],"TUSK":[36.4021,-115.3566],"YOSE":[37.8413,-119.5428],
"DEVA":[36.5668,-117.1388],"CACO":[42.0503,-70.0873],"GATE":[40.5986,-73.8571],"VALL":[35.9181,-106.5106],
"GLCA":[37.3980,-110.8021],"TUAI":[32.4549,-85.6786],"NERI":[37.8970,-81.0429],"PUHO":[19.4092,-155.8978],
"CHIC":[34.4555,-96.9977],"CRMO":[43.4044,-113.5061],"CARE":[38.1706,-111.1427],"LAKE":[36.2446,-114.3805],
"MORA":[46.8547,-121.7064],"AZRU":[36.8355,-108.0017],"MANZ":[36.7270,-118.1530],"ZION":[37.2795,-113.0457],
"JODA":[44.5383,-119.6483],"GOGA":[37.9468,-122.6876],"EFMO":[43.0914,-91.2083],"HALE":[20.6994,-156.1326],
"ARCH":[38.7079,-109.5955],"BELA":[65.9227,-164.1741],"YELL":[44.5830,-110.4901],"MOJA":[35.0972,-115.5394],
"DENA":[63.3263,-150.6030],"ORCA":[42.1046,-123.4043],"SEKI":[36.6857,-118.5772],
"WASO":[38.8939,-77.0427],"CRAD":[38.8939,-77.0427],"RTCA":[38.8939,-77.0427],"NRSS":[38.8939,-77.0427],
"AKRO":[61.2172,-149.8862],"SWAN":[61.2163,-149.8949],"IMRO":[39.7008,-105.1426],"NERO":[39.9517,-75.1610],
"PWRO":[37.7963,-122.4009],"JUBA":[37.9368,-122.3428],"MWAC":[40.8138,-96.6996],"HPTC":[39.3663,-77.3882],
"NTIR":[35.6691,-105.9266],"CHBA":[38.9786,-76.4928],"KLMN":[42.1856,-122.6899],"MOJN":[35.9766,-114.8386],
"SIEN":[36.4388,-118.9045],
}

REGIONS = {"PWR":"Pacific West","IMR":"Intermountain","WASO":"National (WASO)","NER":"Northeast",
           "AKR":"Alaska","SER":"Southeast","MWR":"Midwest"}

# Short program labels keyed off the CFDA/assistance listing in the source file.
def prog(listing):
    s = (listing or '').strip()
    if s.startswith('15.931'): return 'Youth and veteran conservation corps'
    if s.startswith('15.946'): return 'Cultural resources management'
    if s.startswith('15.011'): return 'Experienced Services Program'
    if s.startswith('15.945'): return 'Research and training (CESU)'
    if s.startswith('15.944'): return 'Natural resource stewardship'
    if s.startswith('15.954'): return 'Conservation, outreach, and education'
    if s.startswith('15.935'): return 'National Trails System'
    if s.startswith('15.955'): return 'MLK Historic Site preservation'
    return 'Other'

def unmojibake(s):
    """Repair text whose UTF-8 bytes were decoded as cp1252 on the way into the file.

    This is where the stray a-hat sequences come from: an apostrophe written as
    UTF-8 (E2 80 99) read back one byte at a time through cp1252 becomes three
    visible characters. Re-encoding those characters to their original bytes and
    decoding as UTF-8 puts it back.

    cp1252 leaves five byte values unmapped (0x81, 0x8D, 0x8F, 0x90, 0x9D). A
    string can contain both a character that only cp1252 round-trips and one of
    those raw bytes, so the encode falls back per character instead of per
    string; encoding the whole string with one codec misses those cells. Run
    until stable, because some cells were mangled twice.
    """
    def to_bytes(text):
        out = bytearray()
        for ch in text:
            try:
                out += ch.encode('cp1252')
            except UnicodeEncodeError:
                if ord(ch) > 0xFF:
                    raise
                out.append(ord(ch))          # raw C1 byte cp1252 does not map
        return bytes(out)

    prev = None
    while prev != s:
        prev = s
        try:
            s = to_bytes(s).decode('utf-8', errors='strict')
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
    return s

def clean(v):
    if v is None: return ''
    s = unmojibake(str(v))
    s = s.replace('\u00a0', ' ').replace('\u202f', ' ').replace('\u2009', ' ')  # nbsp variants
    s = s.replace('\u2011', '-')                                              # non-breaking hyphen
    s = re.sub(r'\s+', ' ', s).strip()
    return s

CSV = os.path.join(ROOT, 'data', 'nps-disapprovals-2026.csv')

def load_rows():
    """Prefer the source workbook. It is gitignored, so a fresh clone rebuilds
    from the published CSV instead, which carries the same columns."""
    if os.path.exists(SRC):
        wb = openpyxl.load_workbook(SRC)
        ws = wb['Disapprovals list']
        return [r for r in ws.iter_rows(min_row=2, values_only=True)
                if r[1] is not None and str(r[0]).strip() == 'Disapproved'], 'workbook'
    import csv as _csv, datetime as _dt
    out = []
    with open(CSV, encoding='utf-8-sig', newline='') as fh:
        for d in _csv.DictReader(fh):
            date = None
            if d['doi_decision_date']:
                date = _dt.datetime.strptime(d['doi_decision_date'], '%Y-%m-%d')
            out.append(('Disapproved', int(d['fast_id']), d['region_code'], d['unit_code'],
                        d['recipient'], d['title'], d['assistance_listing'], 'N', date,
                        d['project_abstract'], d['project_impact'], d['review_notes']))
    return out, 'csv'

rows, source_kind = load_rows()

recs = []
for r in rows:
    notes = clean(r[11])
    reversed_ = 'Approved to proceed' in notes
    m = re.findall(r'up to \$([\d,]+\.\d\d)', notes)
    amt = float(m[-1].replace(',','')) if m else None
    d = r[8]
    recs.append({
        'id': int(r[1]),
        'status': clean(r[0]),
        'region': clean(r[2]),
        'unit': clean(r[3]),
        'recipient': clean(r[4]),
        'title': clean(r[5]),
        'prog': prog(r[6]),
        'listing': clean(r[6]),
        'date': d.strftime('%B %-d, %Y') if hasattr(d,'strftime') else clean(d),
        'abstract': clean(r[9]),
        'impact': clean(r[10]),
        'notes': notes,
        'rev': reversed_,
        'amt': amt,
    })

def _fmt_iso(display_date):
    """The records carry a display date; the CSV carries ISO 8601."""
    import datetime
    for fmt in ('%B %d, %Y', '%Y-%m-%d'):
        try: return datetime.datetime.strptime(display_date, fmt).strftime('%Y-%m-%d')
        except (ValueError, TypeError): pass
    return display_date or ''

# Deterministic order, so the two build paths and any rebuild produce identical output.
recs.sort(key=lambda r: (r['unit'], r['id']))

units = {}
for rec in recs:
    u = rec['unit']
    if u not in units:
        units[u] = {'code': u, 'name': NAMES.get(u, u), 'region': rec['region'],
                    'll': LATLON.get(u),
                    'kind': 'park' if u in PARKS else 'office',
                    'place': PLACE.get(u, ''), 'n': 0, 'rev': 0}
    units[u]['n'] += 1
    if rec['rev']: units[u]['rev'] += 1


payload = {
    'recs': recs,
    'units': sorted(units.values(), key=lambda u: (-u['n'], u['name'])),
    'regions': REGIONS,
}
json.dump(payload, open(OUT, 'w'))

# ---------------------------------------------------------------------------
# Public CSV. Built from the cleaned records only: no workbook metadata, no
# About sheet, nothing describing how the records were obtained.
# ---------------------------------------------------------------------------
import csv as _csv
CSV_OUT = os.path.join(ROOT, 'data', 'nps-disapprovals-2026.csv')
COLS = ['fast_id','status','region_code','region_name','unit_code','unit_name','unit_type',
        'mapped_place','latitude','longitude','recipient','title','assistance_listing',
        'program','doi_decision_date','project_abstract','project_impact','review_notes','amount_usd']
# utf-8-sig: the BOM is what makes Excel on Windows read the accented and curly
# characters correctly instead of showing mojibake of its own.
with open(CSV_OUT, 'w', encoding='utf-8-sig', newline='') as fh:
    w = _csv.DictWriter(fh, fieldnames=COLS, lineterminator='\n')
    w.writeheader()
    for r in recs:
        u = units[r['unit']]
        ll = LATLON.get(r['unit'], ['',''])
        w.writerow({
            'fast_id': r['id'], 'status': r['status'],
            'region_code': r['region'], 'region_name': REGIONS.get(r['region'], r['region']),
            'unit_code': r['unit'], 'unit_name': u['name'],
            'unit_type': 'park unit' if u['kind'] == 'park' else 'office, program, or network',
            'mapped_place': u['place'] or u['name'],
            'latitude': ll[0], 'longitude': ll[1],
            'recipient': r['recipient'], 'title': r['title'],
            'assistance_listing': r['listing'], 'program': r['prog'],
            'doi_decision_date': _fmt_iso(r['date']),
            'project_abstract': r['abstract'], 'project_impact': r['impact'],
            'review_notes': r['notes'], 'amount_usd': r['amt'] if r['amt'] else '',
        })
print('wrote', CSV_OUT)

print('source:', source_kind)
print('records', len(recs))
print('offices', sum(1 for u in units.values() if u['kind']=='office'))
print('missing coords', [u['code'] for u in units.values() if not u['ll']])
print('units', len(units), 'with coords', sum(1 for u in units.values() if u['ll']))
print('disapproved', sum(1 for r in recs if r['status']=='Disapproved'))
print('reversed', sum(1 for r in recs if r['rev']))
print('programs', sorted(set(r['prog'] for r in recs)))
print('missing name', sorted(set(u for u in units if u not in NAMES)))
