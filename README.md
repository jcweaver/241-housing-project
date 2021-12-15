#  How Neighborhood Majority Race Impacts Home Value

## Does seeing a neighborhood change perceptions of value?

### Brody Cormier, Ginny Perkey, Amanda Smith, Joanie Weaver
---
## Contents

* [Experiment](#experiment)
* [Data](#data)
* [Analysis](#analysis)
* [Timeline](#timeline)
---
## Experiment

**Research Question**: Does implicit bias regarding how majority nonwhite and majority white neighborhoods look affect the perceived value of those neighborhoods?

**Hypothesis**: When presented with otherwise equal-in-value neighborhoods, street view make a respondent more likely to select the white neighborhood as “higher value.”

In order to test our hypothesis, we designed an experiment in which participants:

* Are given information about two very similar properties in different neighborhoods within the same county.
* Asked which property has a higher value.
* Asked how much more the higher value property is worth, in dollars.

Participants in the **control** group are only shown a table of information about the properties and their neighborhoods.

The **treatment** group is shown this table as well as an embedded Google Street View for each of the two neighborhoods.

The street view is intended to serve as a proxy for seeing a neighborhood in person, the way that an appraiser would. We expect that this will be a source of implicit bias. 

For more information, see the following links:

* [A detailed description of the experiment, along with research that informed its design](https://docs.google.com/document/d/1Qs5hb1kP3awQljCJlnm0N_khagjB0PDHCWRnB5MqnfM/edit#heading=h.la1ebpwwuy3e)
* [A presentation about the experiment, and the results of a pilot study](https://docs.google.com/presentation/d/1sye7xdUww-SUqu3m22Xp4Bh-P0B75o5djAzGNQdRRjs/edit#slide=id.g10692301cd0_0_0)
* [A preview of the Qualtrics survey](https://berkeley.qualtrics.com/jfe/preview/SV_3VpBucuTl1vyOwe?Q_CHL=preview&Q_SurveyVersionID=current)
* [The survey](https://berkeley.ca1.qualtrics.com/surveys/SV_3VpBucuTl1vyOwe/edit)
* [IRB proposal documents](https://drive.google.com/drive/u/1/folders/1Xmkixn9Ew4H8yYJCI5x_PZCzYekRhfb6)

--- 
## Data

---
## Analysis

---
## Timeline

**Idea Formulation: September-October 2021**

* 9/12: Joanie [proposed initial ideas](https://ucbischool.slack.com/archives/C02EC0G0Y0Z/p1631484029019200) for an experiment to look at how appraiser response rate varied by neighborhood.

* 9/14: [First group meeting](https://docs.google.com/document/d/15jMSsCHvC7b52uFkylXv8LckRyQSsf7iF4Aeyqs9exE/edit) to discuss [3-4 project ideas](https://docs.google.com/document/d/1lqvz4oam5KJY3640o5IvrC_qyajcG3QTqaeGIgHXj6k/edit).

* 9/22: [Team meeting to discuss experimental design.](https://docs.google.com/document/d/16hi2VBOn5Qj4dAhTFibg6UndXg4-yMSrBOuWayT1K6E/edit) 
  * Selected a variation of the fourth idea submitted, "Will prospective buyers assign lower values to homes with racial equity signs?"
  * Revised the research question to focus on implicit bias of anyone valuing properties.
  * Decided to use street view as treatment, instead of homes with racial equity signs. This was inspired by [this interactive NYTimes piece](https://www.nytimes.com/interactive/2021/upshot/trump-biden-geography-quiz.html).
  * Joanie assigned to work on creating pairs of comparable neighborhoods based on Census data, match on factors such as population density, average house size, walkability, etc.

* 10/5: [Meeting with Alex](https://docs.google.com/document/d/1Kj8vG0eR4QJo8Its97pF56B3x7OSYEcrZ_uPrrjm1QE/edit) to discuss project idea.
  * Decided to do some initial signal testing to determine what race people associate with the street view of a neighborhood
  * Chose Qualtrics for the survey and discussed randomization within Qualtrics
  * Talked about several other ideas that we have not, as of December 2021, implemented

**Initial Survey Creation**

* 10/17: [Joanie used census data to identify pairs](https://docs.google.com/document/d/1v4HNeZODqUlKigHOstvk2H5Dj2hG_AhYURkBf-5ZVos/edit)
  * Census pairing process documented [here](./ACS_gathering/README.md)
  * Information about school districts was challenging to find, so Amanda assigned to look at third party school ratings
  * Debated different ways to structure questions in survey

10/21: Submitted [Project Check-in](https://docs.google.com/document/d/1HQSpoV4Xwt4ED-7ePKtuLG_Yhvbw8dX5C-XhtpS-0gk/edit#heading=h.vrd68e85s9bq), which summarizes progress at this point, as well as open questions

10/28: [Meeting to discuss city pairs and survey creation](https://docs.google.com/document/d/1grWH5LNwAeQ8CtdjXqsL6DvVZu2nqPD_ULRoEfzSzwc/edit)
  * Decided to use a census tract as a proxy for neighborhood
  * Discussed where to start the street view within the tract (did not resolve)
  * Discussed signal testing with Mechanical Turk

11/3: [IRB proposal submitted; signal testing delayed due to issues with embedding streetview](https://docs.google.com/document/d/1A4QrTHGqPtUDDVIcVDIwCWv1LgqrLM82iNq2RUrWNrk/edit)
  * Completed [IRB proposal](https://drive.google.com/drive/u/1/folders/1Xmkixn9Ew4H8yYJCI5x_PZCzYekRhfb6) for submission
  * Challenging to embed Google Maps JavaScript API into Qualtrics questions
  * This caused delay in signal testing survey
  * Joanie proposes using Observable to create iframes to embed in Qualtrics questions

**Signal Testing Survey**

11/8: Brody created [this survey](https://berkeley.ca1.qualtrics.com/survey-builder/SV_6ExZvJjhhkRKpr8/edit) for determing the race that people associated with our neighborhoods. In creating this, he noticed that some of the census tracts were not residential, so he excluded these from the survey. 

11/9: [Meeting with Alex](https://zoom.us/rec/share/ICrB_-JhS3bMXF4V4yCeSH7yz-MHoa5fi02ig_ueR8LzIQZUf7p-KvQEMWt-rWdX.FHKd4aAbdAdaCgKC)
  * Discussed funding for the class
  * Decided to save funding for pilot survey and actual experiment
  * Sent signal testing survey to friends, family, and Berkeley Slack

11/15: [Realized census definition of race impacts our pairs](https://docs.google.com/document/d/1vleFqYG_0736D88obTgoW4Ea49HrtqlNMX4Kq8t4qlU/edit)
  * Many of our pairs were actually both majority Hispanic
  * Amanda assigned to review signal testing data
  * Ginny assigned to create the main survey
  * Joanie offered to change the views of the streetview so that they begin on something that is more indicative of the race of the neighborhood, such as a person

11/16: Ginny created survey [here](https://berkeley.ca1.qualtrics.com/survey-builder/SV_9YUeotM4pGT6fUa/edit)

11/17: Amanda finished analysis of signal testing data
  * None of the remaining images had a majority “non white” response
  * We only had one pair where people were more likely to recognize the diverse neighborhood as nonwhite than the white neighborhood
  * This finding supports our decision to update the streetview starting points

11/17: Joanie updated the streetview starting locations. 
  * Rationale for the starting location of the streetview documented [here](https://docs.google.com/spreadsheets/d/1aVjiMD6qnfF6uO2XnQpxOYheZSv8s8kReOAo5ZDvQ2M/edit#gid=2056015774) in column O

11/20: Ginny created code to generate survey questions.
  * Calculated bedrooms and bathrooms based off of the median rooms per household, and kept them the same for each property
  * Calculated the square feet off of the bedrooms and bathrooms and have a small random offset to make the properties a tiny bit different from each other
  * The year built is just a random year within a certain range and a small offset.

**First Pilot Run**

11/29: Began reviewing results of first pilot run

11/30: Meeting with Alex ([Zoom recording](https://zoom.us/rec/share/ICYqFt6Oj9YuQ5qHhjE8FqcEaM1Sm5TucRpLVlOvIl0gjriVyIc72nSiHHljZEWY.dQuZ4b6Aym48dsYo), [meeting notes](https://docs.google.com/document/d/1zfC04zIHiQkqeJh-_X4UrQQ-OFehoScf6T8bkXScj9c/edit))
  * Talked about different approaches for modeling
  * Decided to use information given about the properties and the neighborhoods as covariates in the model in order to control for artificially created variation in square footage and year built

12/1: Brody created a dataset that joined the responses to Qualtrics questions with information about the properties and neighborhoods

12/1: [Meeting to review results from pilot run](https://docs.google.com/document/d/1mMjQq7rL9WTuOLaEz_ctsrSE1M2nU2GZ3E8QYScCvUQ/edit)
  * Noticed duplicate rows in the joined dataset
  * Checked proportion of answers in question to see if any were skewed to one property or another
  * Determined that there were several properties that were
  * Noticed that there was an issue with the tables in the survey in that some of the values in treatment were different from the values in countrol

**Survey Refinement and Data Cleaning**

12/1: Ginny changed the information in the tables in the survey. 
  * Changed values to correct skew. In each pair, neither property was allowed to have both higher square footage and a more recent build date.
  * Made sure that the information in the control questions was exactly the same as the information in the treatment questions
  * Note: because of the issue of inconsistency between treatment and control values, as well as the subsequent changes to questions, the pilot data cannot be used for modeling.

12/1: Joanie made the following changes to the dataset:
  * Filtered out rows where the property != Property (i.e. removed rows where the user input property was not equal to the other property column)
  * Added a new column for the white_value_diffassuming a property is white (i.e. if this is negative, that means a person guessed the nonwhite property)
  * Added a column based on whether the streetview for user input property had a person in it
  * Added a column with 1/0 if user input property white or not

**Second Pilot Run**

12/3: Second round of data collection on Mechanical Turk begins.

12/6: Brody worked on data cleaning and modeling.
  * Updated the data set to use the most recent turk results and neighborhood data
  * Removed the duplicate rows and added more of the demographics data as well.
  * Only included a subset of the questions that are required so our data isn't filled with nulls, but if we want any of those conditional questions we can go back and add them. 
  * Noted that the "average" MTurk worker doesn't have much real estate experience.  
  * Added basic models with fixed effects for the survey takers.
  * In this version of the dataset,  demographic_race represents the race of the survey taker and nb_race is the race of the neighborhood they chose

12/7: [Meeting to discuss modeling and analysis](https://docs.google.com/document/d/1J02UH6TaZRE2sw3IaMu33FaB8lnVVVv4twgNbqH9be0/edit)
  * Brody shares information about models he created: 
      * neighborhood is white ~ treatment + survey taker id
      * Cluster by survey taker across all questions
  * Ginny proposes a model with data aggregated by questions

12/8: Amanda works on covariate balance check - [see slide 11](https://docs.google.com/presentation/d/1sye7xdUww-SUqu3m22Xp4Bh-P0B75o5djAzGNQdRRjs/edit#slide=id.g10692301cd0_0_53).
  * Std mean diff is the difference in means divided by the standard deviation of the entire population. Directionally, treatment minus control.

12/8: Ginny creates dataset aggregated by question and two new models using this dataset:
  * average proportion of white neighborhood selected as the outcome variable and treatment as the independent variable
  * model above with question information included as covariates

12/9: Joanie added a model that filters the data to 5 pairs with black/white, excluding asian/white and hispanic/white pairs. This results in a larger treatment effect.

12/9: Feedback from Alex suggests that clustering on the survey takers messes up randomization, and should not be done.

**Proposed Future Work** 

12/9: Brody proposes that in the next version of the survey, we add questions with neighborhoods that are white/white, non-white/non-white in order to use this as a "pre-test" fixed effect for each respondent.

12/13: Joanie notes that we may be able to pull different race percentages at the Census block group level, which is smaller than the tract. This may help create additional pairs.
