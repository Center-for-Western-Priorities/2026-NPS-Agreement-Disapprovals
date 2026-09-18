# Data dictionary

`data/nps-disapprovals-2026.csv` — 133 rows, 19 columns, UTF-8, comma-delimited,
LF line endings. One row per disapproved agreement request.

| Column | Description |
|---|---|
| `fast_id` | Unique identifier for the agreement submission in FAST, the NPS Financial Assistance Submission Tracker |
| `status` | Status as of the August 24, 2026 snapshot. Always `Disapproved` in this file; see [METHODOLOGY.md](METHODOLOGY.md) for the records excluded |
| `region_code` | NPS region code as recorded: PWR, IMR, WASO, NER, AKR, SER, MWR |
| `region_name` | The region code expanded |
| `unit_code` | Four-letter code of the park, office, or program that submitted the request. Park codes resolve at `nps.gov/<code>` |
| `unit_name` | Full name of that unit, office, or program |
| `unit_type` | `park unit`, or `office, program, or network` |
| `mapped_place` | For an office, program, or network: the city its marker sits in. For a park: the park name |
| `latitude`, `longitude` | Decimal degrees, WGS 84. Parks use the NPS boundary centroid; offices use their published address. These are the true coordinates, not the nudged marker positions the map draws |
| `recipient` | The partner organization that would have received the funds |
| `title` | Title of the proposed project |
| `assistance_listing` | The assistance listing (CFDA) category, as recorded |
| `program` | Plain-language label for that listing, used by the map's filter |
| `doi_decision_date` | ISO 8601 date DOI recorded its decision. `2026-08-07` for every row here |
| `project_abstract` | Description of the project, verbatim |
| `project_impact` | What disapproval means for resources, public safety, or operations, verbatim |
| `review_notes` | Submission review notes. Dated entries in standard DOI wording, showing the language used for disapprovals |
| `amount_usd` | Dollar amount, where the review notes state one. Empty for 128 of the 133 rows. **Do not total this column** |

## Notes on the text columns

`project_abstract`, `project_impact`, and `review_notes` are reproduced as recorded.
Three things were done to them and nothing else:

1. **Encoding repaired.** Parts of the source arrived with UTF-8 bytes that had been
   read as Windows-1252, so an apostrophe showed up as `â€™`, an en dash as `â€“`,
   and `Honokōhau` as `HonokÅhau`. Each affected run is re-encoded to its original
   bytes and decoded as UTF-8. 76 cells were affected. See `unmojibake()` in
   `build/prep.py`.
2. **Whitespace collapsed.** Runs of spaces, tabs, and newlines become single spaces;
   leading and trailing whitespace trimmed.
3. **Non-breaking characters normalized.** Non-breaking and narrow spaces become
   ordinary spaces; the non-breaking hyphen becomes a hyphen.

No sentence was rewritten, shortened, or supplied. Section, degree, and accented
characters are preserved.
