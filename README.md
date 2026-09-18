# 2026 NPS Agreement Disapprovals

An interactive map of the National Park Service financial assistance agreements the
Department of the Interior disapproved on August 7, 2026. Each marker is a park unit,
regional office, national program, or monitoring network. Click one to read every
disapproved agreement at that location, with the project description and impact
statement as they appear in the records.

Built by the Center for Western Priorities.

## Live map

**https://center-for-western-priorities.github.io/2026-NPS-Agreement-Disapprovals/**

That URL is the map itself, and it is what the WordPress embed points at. It
redeploys on every push to `main`.

## What the map shows

- **133 agreements** still carrying a disapproved status when the database was rechecked on September 9, 2026
- **$25.9 million** in federal funding those agreements would have obligated
- **61 locations** across **seven NPS regions**
- **18 partner organizations**: conservation corps, nonprofits, park friends groups,
  and university research institutes. Three of them account for 112 of the 133
  agreements: the Great Basin Institute (72), National Experienced Workforce
  Solutions (22), and the Student Conservation Association (18)
- **Eight federal assistance listings**, filterable from a collapsed section in the sidebar

Filter by region, search across every field, and download the full dataset as CSV from
the sidebar. A collapsed "Funding category" section filters by federal assistance
listing; it sits below the fold and carries a caveat, because those listings are
accounting categories rather than a description of the work.

Each park the map plots is drawn with a simplified outline of its boundary, so a reader
can see the shape and extent of the place an agreement belonged to.

Scroll to zoom, drag to pan, and use the region buttons to jump between the lower 48,
Alaska, and Hawaiʻi. Markers hold a constant size as you zoom, so zooming separates
overlapping locations rather than magnifying them.

Inside an iframe the plain scroll wheel is left to the host page, so readers are not
trapped at the map partway down an article. Ctrl and scroll, or cmd and scroll on a
Mac, zooms there; the map says so the first time someone scrolls over it.

The source records hold 140 requests from the August 7 batch. Seven are excluded here
because they no longer carry a disapproved status: four were approved on DOI re-review
on August 20, and three are marked Cancelled, FA Processing, and Pending NPS/DOI
Review. When describing this map in writing, the accurate phrasing is "133 agreements
disapproved on August 7 and still disapproved as of September 9." See
[docs/METHODOLOGY.md](docs/METHODOLOGY.md).

## The data

[`data/nps-disapprovals-2026.csv`](data/nps-disapprovals-2026.csv) is the published
dataset: 133 rows, 19 columns, including coordinates and the full description and
impact text for every agreement. Columns are documented in
[docs/DATA-DICTIONARY.md](docs/DATA-DICTIONARY.md).

Every record carries the federal funding its action would have obligated, from a
second FAST extract. The 133 mapped agreements total **$25,947,857**. The map shows
that total in the footer, per location in the detail panel, and per agreement on a
"Funding blocked" badge, and all three follow the filters.

Ten IDs in the funding extract have no matching record in the disapprovals workbook
and are excluded; they would add $4,995,244. See
[docs/METHODOLOGY.md](docs/METHODOLOGY.md).

## Repository layout

```
index.html                     the built site, one file, ~375 KB
assets/logo/                   CWP logo, SVG; the mark is also inlined in the page
build/
  prep.py                      records  ->  data/disapprovals.json + the published CSV
  build.py                     data + template  ->  index.html
  fetch_boundaries.py          NPS boundary service  ->  simplified park outlines
  template.html                page markup, styles, and behavior
  vendor/                      Leaflet's stylesheet and the park outlines, both
                               inlined at build time
data/
  nps-disapprovals-2026.csv    the published dataset
  disapprovals.json            processed records and marker coordinates
docs/
  METHODOLOGY.md               what is counted, what is excluded, known limits
  DATA-DICTIONARY.md           every CSV column, and what was done to the text
  PLACEMENTS.md                where each non-park marker sits, and the source for it
embed/
  wordpress-snippet.html       paste-ready Custom HTML block
```

## Rebuilding

Requires Python 3 and `openpyxl`. No JavaScript toolchain and no build step at serve
time.

```bash
pip install openpyxl
python build/prep.py     # records   ->  data/disapprovals.json, data/nps-disapprovals-2026.csv
python build/build.py    # data      ->  index.html
```

`prep.py` reads the source workbook when it is present and the published CSV
otherwise, so a fresh clone builds without it. Both scripts print a summary; check the
record count before committing a rebuilt `index.html`.

`fetch_boundaries.py` is separate and is the only script that uses the network. It
rewrites `build/vendor/nps-boundaries.json`, which is committed, so the two build steps
above run offline. Rerun it only when the set of mapped parks changes.

To change the design or behavior, edit `build/template.html` and rerun `build.py`.
Editing `index.html` directly works, but the next build overwrites it.

## Hosting and embedding

`index.html` is a single file. It pulls Leaflet from cdnjs, the Google Fonts
stylesheet, and basemap tiles from Esri's Light Gray Canvas service; everything else,
including the data and Leaflet's own CSS, ships inside the page. No API key and no
build step at serve time, so it runs from anywhere that serves static files. If the
tile service is unreachable the markers still draw over a plain grey field.

**GitHub Pages**, which is what serves the live map above. Settings → Pages →
Source "Deploy from a branch", branch `main`, folder `/ (root)`.

**Netlify.** Import this repository, leave the build command empty, set the publish
directory to `/`.

**WordPress.** Publish the site, then paste
[embed/wordpress-snippet.html](embed/wordpress-snippet.html) into a Custom HTML block
and replace `HOSTED_URL` with the published URL. The snippet carries an optional
auto-height script; without it the frame uses a fixed height and the map scrolls
internally. Both work.

The page is built to sit in a frame: the layout fills its container, the sidebar and
detail panel scroll on their own, and nothing navigates the parent page. On a phone the
sidebar starts collapsed so the map is what loads first.

Note that the CSV download link is relative, so it resolves against wherever
`index.html` is served from. Keep `data/nps-disapprovals-2026.csv` alongside it.

## Sources

- Agreement records: NPS FAST financial assistance tracking, status as of September 9, 2026
- Park coordinates and outlines: [NPS Land Resources Division Boundary and Tract Data Service](https://services1.arcgis.com/fBc8EJBxQRMcHlei/ArcGIS/rest/services/NPS_Land_Resources_Division_Boundary_and_Tract_Data_Service/FeatureServer), layers 0 and 2
- Office locations: addresses published by NPS, listed individually in [docs/PLACEMENTS.md](docs/PLACEMENTS.md)
- Basemap: [Esri Light Gray Canvas](https://services.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Light_Gray_Base/MapServer), credited to Esri, HERE, Garmin, and OpenStreetMap contributors

Center for Western Priorities · [westernpriorities.org](https://westernpriorities.org)
