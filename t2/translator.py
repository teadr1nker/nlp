#!/usr/bin/python3
import json
import re

# load in the dictionary
with open('dictionary.json') as f:
    dictionary = json.load(f)

print(dictionary)
path = 'Зайкина избушка.txt'

with open(path, 'r') as f:
    text = f.read().replace('\n', ' ')

words = re.split(' |,|!|\?|\.', text)
translated = []

limit = len(words)
print(words[:limit])
for word in words:
    if word:
        if word.lower() in dictionary:
            translated.append(dictionary[word.lower()])
        else:
            translated.append(f'[{word}]')

        if limit < 1:
            break
    limit -= 1

for word in words[:limit]:
    print(word, end=" ")
print()

for word in translated:
    print(word, end=" ")
print()
