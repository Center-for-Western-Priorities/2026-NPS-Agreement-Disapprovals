# Marker placements

Two kinds of marker appear on the map.

**Circles** are park units, drawn at the unit's boundary centroid from the
[NPS Land Resources Division Boundary and Tract Data Service](https://services1.arcgis.com/fBc8EJBxQRMcHlei/ArcGIS/rest/services/NPS_Land_Resources_Division_Boundary_and_Tract_Data_Service/FeatureServer),
layer 0. No park coordinate was estimated.

**Squares** are regional offices, national programs, directorates, a historic trail,
and inventory and monitoring networks. None has a park boundary. Each is drawn at the
office address NPS publishes for it, geocoded through OpenStreetMap Nominatim. The
detail panel names the city so a square is never mistaken for a park.

## Square markers

| Code | Entity | Mapped at | Address source |
|---|---|---|---|
| AKRO | Alaska Regional Office | Anchorage, AK | 240 West 5th Avenue — [NPS contact information](https://www.nps.gov/aboutus/contactinformation.htm) |
| IMRO | Intermountain Regional Office | Lakewood, CO | 12795 West Alameda Parkway — [NPS contact information](https://www.nps.gov/aboutus/contactinformation.htm) |
| NERO | Northeast Regional Office | Philadelphia, PA | 1234 Market Street — [NPS contact information](https://www.nps.gov/aboutus/contactinformation.htm) |
| PWRO | Pacific West Regional Office | San Francisco, CA | 555 Battery Street — [NPS contact information](https://www.nps.gov/aboutus/contactinformation.htm) |
| WASO | Washington Support Office | Washington, DC | 1849 C Street NW — [NPS contact information](https://www.nps.gov/aboutus/contactinformation.htm) |
| MWAC | Midwest Archeological Center | Lincoln, NE | 100 Centennial Mall North — [MWAC contact page](https://www.nps.gov/orgs/1740/contactus.htm) |
| HPTC | Historic Preservation Training Center | Frederick, MD | 4801A Urbana Pike — [HPTC contact page](https://www.nps.gov/orgs/1098/contactus.htm) |
| NTIR | National Trails Office | Santa Fe, NM | 1100 Old Santa Fe Trail — [National Trails Office contact page](https://www.nps.gov/orgs/1453/contactus.htm) |
| CHBA | Chesapeake Bay Office / Chesapeake Gateways | Annapolis, MD | [Chesapeake Bay Watershed contact page](https://www.nps.gov/locations/chesapeakebaywatershed/contactus.htm) |
| JUBA | Juan Bautista de Anza National Historic Trail | Richmond, CA | 440 Civic Center Plaza — [Anza trail contact page](https://www.nps.gov/juba/contacts.htm) |
| KLMN | Klamath I&M Network | Ashland, OR | Southern Oregon University, 1250 Siskiyou Blvd — [Klamath Network contact page](https://www.nps.gov/im/klmn/contactus.htm) |
| MOJN | Mojave Desert I&M Network | Boulder City, NV | 601 Nevada Highway — [Mojave Desert Network contact page](https://www.nps.gov/im/mojn/contactus.htm) |
| SIEN | Sierra Nevada I&M Network | Three Rivers, CA | Sequoia and Kings Canyon HQ, 47050 Generals Highway — [Sierra Nevada Network contact page](https://www.nps.gov/im/sien/contactus.htm) |
| CRAD | Cultural Resources Directorate | Washington, DC | **No separate published address.** Carried under WASO in the source file; placed at NPS headquarters. |
| NRSS | Natural Resource Stewardship and Science | Washington, DC | **No separate published address.** Carried under WASO in the source file; placed at NPS headquarters. See the note below. |

`CRAD` is identified as the Cultural Resources Directorate from its own project
abstract, which names that directorate directly. `CHBA` is identified as the
Chesapeake Bay Office from its abstracts, which repeatedly name the Chesapeake
Gateways Network.

### Open question on NRSS

The Natural Resource Stewardship and Science directorate runs much of its work out of
Fort Collins, Colorado, and no address is published for the directorate as such. Its
four agreements are placed at headquarters because the source file files them under
WASO. If the submitting office is confirmed to be Fort Collins, change the `NRSS`
entry in `OFFICE_XY` in `build/prep.py` and rerun the build.

Two entities that appear in the source workbook have no marker on this map, because
their only agreements are among the seven excluded records: the Southwest Alaska I&M
Network (Anchorage) and the Rivers, Trails, and Conservation Assistance program.

## Overlap handling

Squares and circles are placed at their true projected positions first. Any group of
markers landing within nine pixels of each other on the 960-pixel map frame is then
spread around the group's center on a small ring, so every marker stays clickable.
The offset is deterministic and applied in `spread()` in `build/prep.py`.

Groups affected by the current data:

- Washington area: WASO, CRAD, NRSS, and the Chesapeake Bay Office
- Lake Mead National Recreation Area and the Mojave Desert Network, which is
  administered from Boulder City on the Lake Mead boundary
- Oregon Caves National Monument and the Klamath Network in Ashland
- Sequoia and Kings Canyon and the Sierra Nevada Network, administered from the same
  headquarters
- Golden Gate National Recreation Area, the Pacific West Regional Office, and the
  Anza trail office
- Boston Harbor Islands and Minute Man
