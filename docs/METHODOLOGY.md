# Methodology

## Source

Every record comes from a single extract of NPS FAST financial assistance tracking.
Nothing on the map is derived from any other agreement database, and no record was
added, merged, or edited.

Status was checked twice. The extract carried a status column dated **August 24, 2026**,
and a follow-up check in the same database on **September 9, 2026** reconfirmed all 133
records as still `Disapproved`, with the seven excluded records unchanged. The map and
these documents give September 9 as the status date.

The published form of that extract is
[`data/nps-disapprovals-2026.csv`](../data/nps-disapprovals-2026.csv), documented
column by column in [DATA-DICTIONARY.md](DATA-DICTIONARY.md).

## What is counted

The workbook holds 140 records from the August 7, 2026 batch. The map shows the
**133** whose status is still `Disapproved`. Seven are excluded:

| FAST ID | Unit | Status in the file | Why it is excluded |
|---|---|---|---|
| 1784 | PUHO | Awaiting PR | Review notes: "08/20/2026: DOI re-review complete. Approved to proceed." |
| 3160 | SWAN | Awaiting PR | Same, approved on re-review August 20 |
| 2852 | PWRO | Awarded | Same, approved on re-review August 20 |
| 3208 | WASO | Awarded | Same, approved on re-review August 20 |
| 2838 | WASO | Cancelled | No longer a pending disapproval |
| 2330 | AKRO | FA Processing | No longer a pending disapproval |
| 1817 | RTCA | Pending NPS/DOI Review | Never resolved to a disapproval |

Excluding the four reversals removes two locations from the map entirely: Puʻuhonua o
Hōnaunau and the Southwest Alaska Inventory and Monitoring Network each had a single
agreement in the batch, and both were reinstated.

Anyone describing this map in writing should say "133 agreements disapproved on
August 7 and still disapproved as of September 9," not "133 agreements cancelled."
The distinction matters because four of the August 7 disapprovals were reversed
thirteen days later.

## Text shown in the detail panel

The **Description** and **Project impact** paragraphs are the source `PROJECT.ABSTRACT`
and `PROJECT.IMPACT` values verbatim. No sentence was rewritten, condensed, or
supplied. The only changes are whitespace collapsing and an encoding repair, both
described in [DATA-DICTIONARY.md](DATA-DICTIONARY.md).

The headings name what the fields hold. Earlier drafts used an editorial heading over
the impact text, which has been removed.

## Assistance programs

The eight program labels are plain-language readings of the CFDA listing in
`SUGGESTED.FA.LISTING`. The raw listing string is printed with each agreement in the
detail panel so the mapping is checkable:

| Listing | Label on the map |
|---|---|
| 15.931 Youth and Veteran Organizations Conservation Projects | Youth and veteran conservation corps |
| 15.946 Cultural Resources Management | Cultural resources management |
| 15.011 Experienced Services Program | Experienced Services Program |
| 15.945 Cooperative Research and Training Programs (CESU) | Research and training (CESU) |
| 15.944 Natural Resource Stewardship | Natural resource stewardship |
| 15.954 NPS Conservation, Protection, Outreach & Education | Conservation, outreach, and education |
| 15.935 National Trail System Project | National Trails System |
| 15.955 Martin Luther King Junior National Historic Site and Preservation District | MLK Historic Site preservation |

These are the listings each request was filed under. They are accounting categories,
not a description of the work, and reading them as subject areas will mislead. The four
agreements under Natural Resource Stewardship are not the only natural resource work in
the batch; much of the corps work is natural resource work filed under the corps
listing. The map keeps the filter for anyone who wants it, but puts it in a collapsed
section below region and search, with that caveat stated in the sidebar.

The filter carries no color. Every marker on the map is the same orange, so a
per-listing swatch would have implied an encoding the map does not use, and the first
swatch in the old sequence was the marker orange itself.

## Funding blocked

Every one of the 133 records carries a federal funding figure, from a second FAST
extract giving `FED FUNDING THIS ACTION` by FAST ID. They total **$25,947,857**.

That extract holds 143 rows. 133 match a record on this map exactly, with no record
left without a figure. The other ten IDs (37, 140, 258, 799, 907, 1250, 1355, 1693,
1832, 1942) do not appear in the disapprovals workbook at all, so there is no park,
partner, or project text to attach them to, and they are excluded. Together they
account for a further $4,995,244. If they belong to this batch, the published total
is low by that amount, and resolving them is worth doing before the figure is used in
print.

None of the ten is one of the seven excluded records, so no reversal or cancellation
is double-counted.

An earlier draft parsed dollar amounts out of the free-text review notes. Those
appeared on only five records, four of which were the reversals, and they are no
longer used. The funding column replaces them.

Figures are the amount each action would have obligated, not an appropriation or an
annual budget line. The accurate phrasing is "agreements worth $25.9 million," not
"$25.9 million cut from the Park Service." 

## Counting partner organizations

The `recipient` column holds 29 distinct strings, but several are variants of the same
organization: "The Great Basin Institute," "Great Basin Institute," and "THE GREAT
BASIN INSTITUTE"; three spellings of the Desert Research Institute, two of which route
it through the Nevada System of Higher Education; "National Experienced Workforce
Solutions" with and without the corporate suffix, plus "New Solutions," the trade name
that organization uses ([newsolutions.org](https://newsolutions.org/about-new-solutions/));
and two capitalizations of the Golden Gate National Parks Conservancy. Collapsing those
leaves **18** organizations.

Three of them hold 112 of the 133 agreements, or 84 percent: the Great Basin Institute
(72 agreements, $12,229,710), National Experienced Workforce Solutions (22, $2,076,386),
and the Student Conservation Association (18, $1,344,856).

No tribal government or tribal nonprofit appears in the recipient column. An earlier
version of the README said otherwise; that was wrong.

## Regions

The `Region` column uses the legacy NPS region codes (PWR, IMR, WASO, NER, AKR, SER,
MWR) rather than the numbered Interior regions adopted in 2018. The map preserves the
codes as given and expands them to their legacy names.

## Placement of markers

Park units are drawn at their NPS Land Resources Division boundary centroid. Offices,
national programs, and monitoring networks have no park boundary and are drawn as
squares at the office address NPS publishes for each. Every placement and its source
is listed in [PLACEMENTS.md](PLACEMENTS.md).

Sequoia and Kings Canyon share one administrative unit code (SEKI) and are drawn at
the Sequoia centroid.

Parks the map plots are also drawn with a simplified outline of their boundary,
from layer 2 of the same NPS Land Resources Division service. Those outlines are for
orientation, not survey: Douglas-Peucker simplified with the tolerance capped per
shape so small units keep a recognizable form, interior holes dropped, detached
pieces below a floor dropped, and coordinates rounded to about 11 metres. The largest
piece of every park is always kept, so no park loses its outline. `build/fetch_boundaries.py`
regenerates the file and documents the parameters; the result is committed, so the
build itself never touches the network.

Offices, programs, and networks have no boundary and are drawn only as squares.

Every marker sits at its true coordinate. Markers hold a constant on-screen size
as the map is zoomed, so the circle area encodes the agreement count and zooming
separates neighbouring locations rather than enlarging them. Earlier drafts nudged
overlapping markers apart because the map could not zoom; that is gone, and no
position on the map is adjusted for legibility.

## Known limits

1. Three WASO entries (Cultural Resources Directorate, Natural Resource Stewardship
   and Science, Rivers Trails and Conservation Assistance) have no separately
   published street address and sit at NPS headquarters. NRSS in particular has a
   large operational presence in Fort Collins, Colorado. If the submitting office is
   known, correct `LATLON` and `PLACE` in `build/prep.py`.
2. A monitoring network's work happens across its member parks, not at its office.
   The square marks where the network is administered, which the detail panel states.
3. The status snapshot runs through September 9, 2026. Any later DOI action is not
   reflected.
4. Basemap tiles come from Esri's Light Gray Canvas service. They are the page's
   only external dependency. If the service is unreachable the markers still draw,
   over a plain grey field.
