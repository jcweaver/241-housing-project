## American Community Survey (ACS) & Other Data Collection

### ACS Data Collection & Pairing Files
Below are some files used for collecting data for tracts in the most populous counties using the Census API.

| <div style="width:50px">File name</div> |  <div style="width:150px">Description</div> |
| --- | --- |
| utils.py | Leveraged and modified some code Joanie used for a project with Centri Tech Foundation, this file contains helper functions for calling the Census API |
| 241_Data_Gathering.ipynb | A jupyter notebook that calls the Census API to collect ACS data and merges it with other data sources |
| Pairing.ipynb | A jupyter notebook that takes the results from the data gathering notebook and outputs a csv file of tract/neighborhood pairs and their statistics. This file also has code to add back the latitude/longitude pairs for each neighborhood to help with the initial google maps drop |
| census_tracts_hisp.csv | A csv file output after collecting the ACS variables from the Census API |
| tracts_data_hisp.csv | A file output after cleaning the ACS variables and merging with other data sources from running the full 241_Data_Gathering.ipynb |
| pairings_26.csv |  The result of running the Pairing notebook. This file contains 26 pairs of tracts. |
| pairs_with_latlong.csv | The result of adding latitude/longitude to the pairings_26.csv |
| pairs_with_hisp.csv | The result of adding additional race/ethnicity ACS variables to the pairings_26.csv |


### Additional Datasets
Below are some additional files that need to be downloaded in order to run the Data Gathering & Pairing notebooks as they are not in the Github due to their large size.

| <div style="width:35px">File name</div> | <div style="width:50px">Source </div>| <div style="width:75px">Description</div> |
| --- | --- | --- |
| 2019_Gaz_tracts_national.txt | https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.html | A file mapping census tract IDs to land area to use to calculate population and housing densities. Note because we are pulling data from ACS5 2019, we need to use the 2019 tracts and not the 2020 or 2021 tracts which are slightly different. |
| co-est2019-alldata.csv | https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv | A file containing the population estimates for all counties in the US. This is used to identify the most populous counties. |
| EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv | https://catalog.data.gov/dataset/walkability-index | A file mapping census tract ID to walkability index. This dataset says it uses 2019 Census groups. |
| grf19_lea_tract.xlsx | https://nces.ed.gov/programs/edge/Geographic/RelationshipFiles | A file mapping census tract id to school district name/ID. The link downloads a zip that has this info in a variety of formats, but you should look for the format that references tracts. Note use 2019! |


Note about our "neigborhood" of a Census tract. Some of the data we wanted to query was only available at the tract level so we started this project collecting data at the tract level and pairing based on tracts as our neighborhoods. We believe that additional neighborhoods could be discovered if we update our code to collect data at the block group level, a smaller Census statistical area than the tract. The work required to update our code to use block groups would be:
* Update the utils.py to support calling data for block groups where applicable
* Update the data gathering notebook 

### Working with Census Data
We knew we wanted to be able to evaluate demographic data so we decided to use Census data. There are several levels of statistical areas that the Census provides data for. Census tracts are defined as small, relatively permanent statistical subdivisions of a county, with a minimum population of 1,200 and a maximum population of 8,000. Each census tract/BNA could contain as many as nine BGs (block groups 1 to 9; there is no block group 0). Census blocks, the smallest geographic area for which the Bureau of the Census collects and tabulates decennial census data, are formed by streets, roads, railroads, streams and other bodies of water, other visible physical and cultural features, and the legal boundaries shown on Census Bureau maps. A block group consists of all census blocks whose numbers begin with the same digit in a given census tract or BNA [11]. We chose to use tracts for our initial analysis because they were the smallest statistical area that all of our variables pulled from the American Community Survey (ACS) could provide data for. Note that some of our variables are available to pull at the block group level and that we could use tract level data where block group data is not available. The GEOID for a block group is the 11 digits from the tract (STATE+COUNTY+TRACT) + 1 digit from the BLOCK GROUP.

Sources:
* [Census Tracts](https://www2.census.gov/geo/pdfs/education/CensusTracts.pdf)
* [Census Blocks and Block Groups](https://www2.census.gov/geo/pdfs/reference/GARM/Ch11GARM.pdf)
* [GEOIDs](https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html)

