# ML_project_P09_Smart_solar_power
The project P09 "Smart Solar Power" for Machine Learning course 2021/2022 autumn

**Description**:

>> Electricity and solar power are hot topics at the moment.

Our idea was to take the weather satellite data (from https://www.ilmateenistus.ee/ilm/ilmavaatlused/satelliidipildid/infrapunane-pilt/  or some other data source from that page e.g radar images or natural colors images) and bring the localisation together with the locations of the weather stations (https://meteo.physic.ut.ee/). The data about how much of solar intensity (How many watts per a measurement unit/meter ) there is currently. Per the data perhaps it would be possible to predict the cloudiness in some x,y coordinates in the near future and then predict the solar intensity for that time. The goal is to predict the amount of electricity that can be produced from solar panels, expectedly by small, 5 -minute intervals. This could be used by a "really smart washing machine" that knows the current market price for electricity and also know how much each washing cycle or water heating will cost and perhaps waits for the 10 minutes for when the cheaper electricity may be available from the solar panels on the roof.


**Meeting 11.11.2021**

- Presentation discussion
  - Mart creates the presentation
  - Topics
    - What data we have, how do we use it
    - What is our goal
    - What models we will use/try
    - Materials we have found: previous work
- Discussion about first sight on the data
  - What attribute will be predicted
  - Attributes which impact the most

Next: intermediate presentation on Monday 15.11.2021

Next meeting: 18.11.2021 17:00

**Meeting 18.11.2021**

- We have made some predictions for data loaded from Meteo
- Mart found the closest function for the radiation flux means
- Heidi made data cleansing and trained the cleaned data with Random Forest 

Prediction ideas
- Let's try to predict by month or by season. E.g fit june, predict june.
- Let's try XGBoost
- Heidi creates the function for data cleansing that everybody can use the same set of data.

Next meeting 25.11.2021 17:00

**Meeting 25.11.2021**

- During meeting we dealt with cleansing of the files Mart uploaded to git and we ran the Random Forest on it.
- Siim found some sources where we could get the cloudiness values for predictions. Need to use API.
- No other models yet tried.
- Siim will contact Ott Kekišev to ask more data for predictions as it is not enough to predict the radiation flux. 
  We need also the cloudiness rate and the coefficient of the solar panel.