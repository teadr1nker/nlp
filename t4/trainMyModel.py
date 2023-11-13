#!/usr/bin/python3
from ohe import oneHotEncodingRus
import numpy as np
import pandas as pd
import json

from keras.models import Sequential
from keras.layers import Dense, SimpleRNN
# from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix

data = pd.read_csv('surnames.csv')

print(data)

size = max([len(x) for x in data['surname'].values])

nationalities = list(set(data['nationality']))

N = len(data)
print(f'number of surnames {N}')
print(f'max surname length {size}')
print(f'nationalities {nationalities}')

X = []
Y = []

for i in range(N):
    X.append(oneHotEncodingRus(data['surname'][i], size))
    y = np.zeros(len(nationalities))
    y[nationalities.index(data['nationality'][i])] = 1
    Y.append(y)

X = np.array(X)
Y = np.array(Y)

print(f'X {X.shape} Y {Y.shape}')

model = Sequential()
model.add(SimpleRNN(units=len(nationalities), input_shape=X[0].shape,
                    activation='relu'))
model.add(Dense(128))
model.add(Dense(len(nationalities), activation='softmax'))
model.compile(loss='mean_squared_error')

model.fit(X, Y, epochs=32, batch_size=16)

print(model.evaluate(X, Y))
model.save('mymodel')

settings = {'nationalities': nationalities,
            'size': size}
with open('settings.json', 'w') as f:
    json.dump(settings, f)

# Confusion matrix
YPred = [nationalities[np.argmax(y)] for y in model.predict(X)]
result = confusion_matrix(YPred, data['nationality'].values,
                          normalize='pred', labels=nationalities)

matrixcsv = ''
matrixcsv += ','.join(['error']+nationalities) + '\n'
for i in range(len(nationalities)):
    matrixcsv += nationalities[i] + ',' +\
        ','.join([str(round(s, 2)) for s in result[i]]) + '\n'

with open('confusion.csv', 'w') as f:
    f.write(matrixcsv)
