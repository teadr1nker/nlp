#!/usr/bin/python3
import pandas as pd
from datetime import datetime

print(f'Reading dataset {datetime.now()}')
df = pd.read_csv('lenta-ru-news-small.csv')
print(f'shape of dataset{df.shape}')

texts = df['text'].astype(str).values
del df

print(f'Joining texts {datetime.now()}')

text = ' '.join(texts)

print(f'Saving {datetime.now()}')
with open('bigText.txt', 'w') as f:
    f.write(text)
