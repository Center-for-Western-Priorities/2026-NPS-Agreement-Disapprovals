# Intro text for the WordPress page

Drafted to sit above the embedded map as native page text. Every figure comes from the
published dataset behind the map. Sources and caveats are at the bottom.

---

## Headline options

1. Tracking the national park agreements Interior blocked
2. What the Trump administration blocked at 61 national park sites
3. The $25.9 million in park work Interior stopped in August

## Deck / subhead

An interactive map of the 133 National Park Service partner agreements the Department of the Interior disapproved on August 7, 2026.

---

## Intro, long version (about 280 words)

On August 7, 2026, the Department of the Interior disapproved 133 financial assistance agreements the National Park Service had arranged with outside partners. Those agreements would have obligated $25.9 million in federal funding at 61 parks, regional offices, and programs across all seven Park Service regions. The Washington Post [first reported the disapprovals](https://www.washingtonpost.com/climate-environment/2026/09/11/trump-administration-blocks-25-million-funding-national-parks/) on September 11.

Financial assistance agreements are how the Park Service buys work it cannot staff itself. The blocked agreements cover hazard tree removal, archeological survey, invasive species control, water quality monitoring, trail crews, museum collections care, and seasonal positions filled by conservation corps members and retirees.

Two examples show the range. At Effigy Mounds National Monument in Iowa, an $80,597 agreement with the Forest Stewards Guild would have removed hazard trees from the Sny Magill unit, which holds roughly 106 Native American mounds, the largest concentration known in the United States. Park Service staff wrote that 61 of the trees slated for removal stand within a mound, and that a fall could expose the human remains buried there. At Lake Mead National Recreation Area, a $3.5 million agreement with the Desert Research Institute would have mapped unauthorized roads and surveyed buried cultural resources in areas exposed by falling water levels. It is the largest single agreement in the batch.

The work was concentrated in a small number of partners. Three organizations held 112 of the 133 agreements: the Great Basin Institute, National Experienced Workforce Solutions, and the Student Conservation Association.

The Center for Western Priorities mapped every disapproved agreement using Park Service records. Explore it below.

---

## Intro, short version (about 130 words)

On August 7, 2026, the Department of the Interior disapproved 133 National Park Service agreements with outside partners, blocking $25.9 million in federal funding at 61 parks, offices, and programs in all seven Park Service regions. The Washington Post [first reported the disapprovals](https://www.washingtonpost.com/climate-environment/2026/09/11/trump-administration-blocks-25-million-funding-national-parks/) on September 11.

The agreements covered hazard tree removal, archeological survey, invasive species control, water quality monitoring, trail crews, and seasonal staffing. They ranged from $8,000 to $3.5 million. The largest would have mapped cultural resources at Lake Mead National Recreation Area, where falling water levels have exposed ground that has not been surveyed.

The Center for Western Priorities mapped every disapproved agreement using Park Service records. Explore it below.

---

## How to explore the map

Every circle is a national park site, drawn over the outline of the park itself. Every square is a regional office, program, or monitoring network, each of which supports a group of parks rather than one. Larger markers hold more agreements. Click one to read the project description and the Park Service's own statement of what disapproval means for that site, along with the dollar figure attached to each agreement.

Filter by region in the sidebar, or search across every field. Scroll to zoom, drag to pan. The full dataset is available to download as a CSV.

---

## Pull quote option

"The mounds at Sny Magill will remain at risk from tree fall that might expose the human remains buried within these mounds."
— Park Service impact statement, Effigy Mounds National Monument

---

## Notes for the editor

**On the Washington Post link.** I could not open the story. The site returns a 403 to
automated requests, so I have not read it and nothing above paraphrases its contents.
The headline, date, and URL come from the link Aaron posted in #lookwest on September 12.
Someone should confirm two things before this publishes: that "first reported" is
accurate, and that the Post's figure matches ours. The Post headline says $25 million and
our dataset totals $25,947,857, which is consistent, but the two may be counting
different things.

**On phrasing.** Say "agreements worth $25.9 million," not "$25.9 million cut from the
Park Service." The figure is the federal funding each proposed action would have
obligated, not an appropriation or an annual budget line.

Say "133 agreements disapproved on August 7 and still disapproved as of September 9," not
"133 agreements cancelled." The source batch held 140 requests. Four were approved on
Interior re-review on August 20, and three carry other statuses. A follow-up check of
the database on September 9 reconfirmed all 133 as still disapproved. See
[METHODOLOGY.md](https://github.com/Center-for-Western-Priorities/2026-NPS-Agreement-Disapprovals/blob/main/docs/METHODOLOGY.md).

**One open figure.** A second Park Service funding extract holds ten IDs worth
$4,995,244 that do not appear in the disapprovals workbook at all. If they belong to this
batch, the real total is closer to $30.9 million. Worth resolving before the number goes
in a headline.

**Verified figures used above**

| Claim | Source |
|---|---|
| 133 agreements, $25,947,857, 61 locations, seven regions | `data/nps-disapprovals-2026.csv` |
| Range $8,000 to $3,489,627 | Same file, `fed_funding_this_action` |
| Effigy Mounds: $80,597, Forest Stewards Guild, ~106 mounds, 61 trees within a mound | Project abstract and impact statement, FAST ID for EFMO |
| Lake Mead: $3,489,627, Desert Research Institute, Overton Arm and Government Wash | Project abstract, largest single figure in the file |
| Three partners hold 112 of 133 agreements | Recipient column, name variants collapsed; see METHODOLOGY.md |
