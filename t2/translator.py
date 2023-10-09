#!/usr/bin/python3
import json
import re

# load in the dictionary
with open('dictionary.json') as f:
    dictionary = json.load(f)

print(dictionary)
path = 'Маша и медведь.txt'

with open(path, 'r') as f:
    text = f.read().replace('\n', ' ')

words = re.split(' |,|!|\?|\.', text)
translated = []

limit = 50
print(words[:limit])
for word in words:
    if word.lower() in dictionary:
        translated.append(dictionary[word.lower()])
    else:
        translated.append(f'[{word}]')
    if limit < 1:
        break
    limit -= 1

print(translated)

