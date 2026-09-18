# 2026 NPS Agreement Disapprovals

An interactive map of the National Park Service financial assistance agreements the
Department of the Interior disapproved on August 7, 2026. Each marker is a park unit,
regional office, national program, or monitoring network. Click one to read every
disapproved agreement at that location, with the project description and impact
statement as they appear in the records.

Built by the Center for Western Priorities.

## What the map shows

- **133 agreements** still carrying a disapproved status in the August 24, 2026 snapshot
- **61 locations** across **seven NPS regions**
- **24 partner organizations**: universities, youth and veteran conservation corps,
  tribal organizations, and nonprofits
- **Eight assistance programs**, filterable, each with its own color

Filter by program or region, search across every field, and download the full dataset
as CSV from the sidebar.

The source records hold 140 requests from the August 7 batch. Seven are excluded here
because they no longer carry a disapproved status: four were approved on DOI re-review
on August 20, and three are marked Cancelled, FA Processing, and Pending NPS/DOI
Review. When describing this map in writing, the accurate phrasing is "133 agreements
disapproved on August 7 and still disapproved as of August 24." See
[docs/METHODOLOGY.md](docs/METHODOLOGY.md).

## The data

[`data/nps-disapprovals-2026.csv`](data/nps-disapprovals-2026.csv) is the published
dataset: 133 rows, 19 columns, including coordinates and the full description and
impact text for every agreement. Columns are documented in
[docs/DATA-DICTIONARY.md](docs/DATA-DICTIONARY.md).

Only five of the 133 records carry a dollar figure, and those appear inside free-text
review notes rather than a funding column. There is no defensible funding total and
none is shown.

## Repository layout

```
index.html                     the built site, self-contained, ~280 KB
build/
  prep.py                      records  ->  data/disapprovals.json + the published CSV
  build.py                     data + template  ->  index.html
  template.html                page markup, styles, and behavior
data/
  nps-disapprovals-2026.csv    the published dataset
  disapprovals.json            processed records, marker placements, state geometry
  us-states-albers.json        state outlines, pre-projected to Albers USA
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

To change the design or behavior, edit `build/template.html` and rerun `build.py`.
Editing `index.html` directly works, but the next build overwrites it.

## Hosting and embedding

`index.html` is one file with no external scripts, no tile server, and no API key. It
requests the Google Fonts stylesheet and falls back to Georgia and a system sans if
that is blocked. Serve it from anywhere that does static files.

**GitHub Pages.** Settings → Pages → Source "Deploy from a branch", branch `main`,
folder `/ (root)`.

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

- Agreement records: NPS FAST financial assistance tracking, status as of August 24, 2026
- Park coordinates: [NPS Land Resources Division boundary centroids](https://services1.arcgis.com/fBc8EJBxQRMcHlei/ArcGIS/rest/services/NPS_Land_Resources_Division_Boundary_and_Tract_Data_Service/FeatureServer)
- Office locations: addresses published by NPS, listed individually in [docs/PLACEMENTS.md](docs/PLACEMENTS.md)
- State outlines: [us-atlas](https://github.com/topojson/us-atlas), simplified and projected to Albers USA

Center for Western Priorities · [westernpriorities.org](https://westernpriorities.org)
