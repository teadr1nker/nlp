#!/usr/bin/python3
from ohe import oneHotEncodingRus
import numpy as np
import pandas as pd
import json
import keras


with open('settings.json', 'r') as f:
    settings = json.load(f)


model = keras.models.load_model('mymodel')

while True:
    surname = input('surname: ')
    x = oneHotEncodingRus(surname, settings['size'])
    y = model.predict(np.array([x]))
    print(settings['nationalities'])
    print(list(y[0]))
    print(f'nationality: {settings["nationalities"][np.argmax(y)]}')
