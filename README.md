# ML_project_P09_Smart_solar_power
The project P09 "Smart Solar Power" for Machine Learning course 2021/2022 autumn

**Description**:

> Electricity and solar power are hot topics at the moment.

Our idea was to take the weather satellite data (from [Ilmateenistus](https://www.ilmateenistus.ee/ilm/ilmavaatlused/satelliidipildid/infrapunane-pilt/)  or some other data source from that page e.g radar images or natural colors images) and bring the localisation together with the locations of the weather stations, e.g [E-ilmajaam Tartus füüsikahoone katusel](https://meteo.physic.ut.ee/). The data about how much of solar intensity (How many watts per a measurement unit/meter ) there is currently. Per the data perhaps it would be possible to predict the cloudiness in some x,y coordinates in the near future and then predict the solar intensity for that time. The goal is to predict the amount of electricity that can be produced from solar panels, expectedly by small, 5 -minute intervals. This could be used by a "really smart washing machine" that knows the current market price for electricity and also know how much each washing cycle or water heating will cost and perhaps waits for the 10 minutes for when the cheaper electricity may be available from the solar panels on the roof.

Members:
- Heidi Carolina Martinsaari
- Mart Traagel
- Siim Suitslepp


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

**Meeting 2.12.2021**

- We had a short meeting where we discussed the idea of project again:
  - Data of solar radiation should be loaded somewhere continuosly for the coordinate needed.
  - **Our task** is to create the prediction calculations for the data to forecast the solar intensity.
  - Solar intensity amount and the parameters of solar panels are the input for calculating the energy product.
  - Based on future energy production and future energy price the decisions are made.
- For predicting solar radiance is better to use ARIMA model for time series model.
  - Random Forest as before is not possible to use as we do not have future information about other parameters also.
  - (Timestamp and) Radiation Flux to time series and predictions on it. Worked!
- So, to use the ARIMA model:
  - We have to know what is it: [LINK to topic in general](https://www.sauga.pri.ee/portfolio/EconometricsLectureStationaryTS.pdf)
  - How to use it: [LINK to code example](https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/) and [LINK to documentation](https://www.statsmodels.org/dev/generated/statsmodels.tsa.arima.model.ARIMA.html?highlight=arima#statsmodels.tsa.arima.model.ARIMA)
  - We have to know what is a walk-forward validation: [LINK to validation possibilities](https://machinelearningmastery.com/backtest-machine-learning-models-time-series-forecasting/)
- After reading materials, please experiment with the code in github: **ARIMA.ipynb**
- If we are ready with predicting, lets do somekind of pipeline or procedure.. 
- Meeting with project owner!!! Siim will write an e-mail.