import pandas as pd
import matplotlib.pyplot as plt
import os
import tensorflow as tf
from tensorflow import keras

import math
import keras
import numpy as np
from sklearn.tree import DecisionTreeRegressor


def get_weather_data(start_year, start_month, start_day, end_year, end_month, end_day):
    url = f'https://meteo.physic.ut.ee/et/archive.php?do=data&begin%5Byear%5D={start_year}&begin%5Bmon%5D={start_month}&begin%5Bmday%5D={start_day}&end%5Byear%5D={end_year}&end%5Bmon%5D={end_month}&end%5Bmday%5D={end_day}&9=1&12=1&11=1&14=1&ok=+Esita+p%C3%A4ring+'
    c = pd.read_csv(url)
    c.columns = ['Aeg', 'Temperatuur', 'Niiskus', 'Valgustatus', 'Kiirgusvoog']
    return c


def add_detailed_time(df):
    df['Aasta'] = pd.DatetimeIndex(df['Aeg']).year
    df['Kuu'] = pd.DatetimeIndex(df['Aeg']).month
    df['Päev'] = pd.DatetimeIndex(df['Aeg']).day

    df['Tund'] = pd.DatetimeIndex(df['Aeg']).hour
    df['Minut'] = pd.DatetimeIndex(df['Aeg']).minute

    return df


train = get_weather_data(2011, 1, 1, 2015, 12, 12)


train['Aeg'] = pd.to_datetime(train['Aeg'])
train = add_detailed_time(train)
train.replace(r'^\s*$', 0, regex=True)
train.fillna(0, inplace=True)
train['Kiirgusvoog'] = pd.to_numeric(train['Kiirgusvoog'], errors='coerce', downcast=None)
train['Temperatuur'] = pd.to_numeric(train['Temperatuur'], errors='coerce', downcast=None)
train['Valgustatus'] = pd.to_numeric(train['Valgustatus'], errors='coerce', downcast=None)
train.fillna(0, inplace=True)

valid = get_weather_data(2016, 1, 1, 2017, 12, 12)
valid['Aeg'] = pd.to_datetime(valid['Aeg'])
valid = add_detailed_time(valid)
valid.fillna(0, inplace=True)
valid.replace(r'^\s*$', 0, regex=True)
valid['Kiirgusvoog'] = pd.to_numeric(valid['Kiirgusvoog'], errors='coerce', downcast=None)
valid['Temperatuur'] = pd.to_numeric(valid['Temperatuur'], errors='coerce', downcast=None)
valid['Valgustatus'] = pd.to_numeric(valid['Valgustatus'], errors='coerce', downcast=None)
valid.fillna(0, inplace=True)

# aprill. 22, 15, 45

X_train = train[['Temperatuur', 'Valgustatus', 'Aasta', 'Kuu', 'Päev', 'Tund', 'Minut']]

# nihe 5 min
# kõik lassod ja asjad

y_train = train['Kiirgusvoog']


X_valid = valid[['Temperatuur', 'Valgustatus', 'Aasta', 'Kuu', 'Päev', 'Tund', 'Minut']]
y_valid = valid['Kiirgusvoog']

model = DecisionTreeRegressor(random_state=0)
model.fit(X_train, y_train)
prediction = model.predict(X_valid)

plt.plot(y_valid, label='True')
plt.plot(prediction, label = 'Predictions')
plt.legend()
plt.show()

print(f"Validation accuracy is {model.score(X_valid, y_valid)*100}%")

