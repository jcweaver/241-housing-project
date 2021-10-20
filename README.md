# 241-housing-project

Below are some files used for collecting data for tracts in the most populous counties using the Census API.

* utils.py - Borrowing some code Joanie uses at Centri Tech Foundation, this file contains helper functions for calling the Census API
* data/ - The county/state population file used to find the most populous counties
* 241_Data_Gathering.ipynb - A jupyter notebook that calls the Census API using utils functions and then manipulates the data


Data files:

| <div style="width:100px">File name</div> | <div style="width:250px">Source </div>| <div style="width:250px">Description</div> |
| --- | --- | --- |
| 2019_Gaz_tracts_national.txt | https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.html | A file mapping census tract IDs to land area to use to calculate population and housing densities. Note because we are pulling data from ACS5 2019, we need to use the 2019 tracts and not the 2020 or 2021 tracts which are slightly different. |
| co-est2019-alldata.csv | https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/counties/totals/co-est2019-alldata.csv | A file containing the population estimates for all counties in the US. This is used to identify the most populous counties. |
| EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv | https://catalog.data.gov/dataset/walkability-index | A file mapping census tract ID to walkability index. This dataset says it uses 2019 Census groups. |
| grf19_lea_tract.xlsx | https://nces.ed.gov/programs/edge/Geographic/RelationshipFiles | A file mapping census tract id to school district name/ID. The link downloads a zip that has this info in a variety of formats, but you should look for the format that references tracts. Note use 2019! |
| state_county.csv | Generated from running the jupyter notebook | A list of the county/state pairs of the most populous counties we plan to find the tracts from |



