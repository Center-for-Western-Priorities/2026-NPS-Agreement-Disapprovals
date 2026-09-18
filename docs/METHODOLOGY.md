# Methodology

## Source

Every record comes from a single extract of NPS FAST financial assistance tracking,
with a status column dated August 24, 2026. Nothing on the map is derived from any
other agreement database, and no record was added, merged, or edited.

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
August 7 and still disapproved as of August 24," not "133 agreements cancelled."
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

## Dollar amounts

Only five records in the workbook carry a dollar figure, and those appear inside the
free-text `ABSTRACT.REVIEW.NOTES` field rather than in a funding column. Where a
figure is present it is shown on that agreement. **There is no defensible total, and
none is displayed.** If a funding column exists in another FAST extract, adding it
would be the single biggest improvement to this product.

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

Markers whose projected positions fall within nine pixels of each other are spread
around the group's center on a small ring so each stays clickable. The largest
displacement on the current data is under 12 pixels on a 960-pixel-wide map, roughly
40 miles at the scale of the contiguous states. Affected groups: the four Washington
area entries, Lake Mead with the Mojave Desert Network, Oregon Caves with the Klamath
Network, Sequoia with the Sierra Nevada Network, Golden Gate with two Bay Area
offices, and Boston Harbor Islands with Minute Man.

## Known limits

1. Three WASO entries (Cultural Resources Directorate, Natural Resource Stewardship
   and Science, Rivers Trails and Conservation Assistance) have no separately
   published street address and sit at NPS headquarters. NRSS in particular has a
   large operational presence in Fort Collins, Colorado. If the submitting office is
   known, correct `OFFICE_XY` and `PLACE` in `build/prep.py`.
2. A monitoring network's work happens across its member parks, not at its office.
   The square marks where the network is administered, which the detail panel states.
3. The status snapshot is a single date. Any later DOI action is not reflected.
