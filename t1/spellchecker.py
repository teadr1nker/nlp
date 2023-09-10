#!/usr/bin/python
import json, os, difflib
import numpy as np


# Levenshtein distance
def distance(word, match):

    distances = np.zeros((len(word) + 1, len(match) + 1))

    for t1 in range(len(word) + 1):
        distances[t1][0] = t1

    for t2 in range(len(match) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(word) + 1):
        for t2 in range(1, len(match) + 1):
            if (word[t1-1] == match[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    n = max(len(match), len(word))
    return (n - distances[-1, -1]) / n

# read tokens
with open('words.json') as f:
    tokens = json.load(f)['words']

# print(tokens)
alphabet = 'абвгдеёжзийклмнопрстуфчцчшщъыьэюя'

# spell checker
def checkSpelling(word):
    word = word.lower()
    if word in tokens:
        return word, 'No error!'

    matches = {}

    #adding letter
    for i in range(len(word)+1):
        for letter in alphabet:
            match = word[:i] + letter + word[i:]
            if match in tokens:
                matches[match] = distance(word, match)
    #removing letter
    for i in range(len(word)):
        match = word[:i] + word[i+1:]
        if match in tokens:
            matches[match] = distance(word, match)
    #replace letter
    for i in range(len(word)):
        for letter in alphabet:
            match = word[:i] + letter + word[i+1:]
            if match in tokens:
                matches[match] = distance(word, match)
    #swap two letters
    for i in range(len(word)-1):
        wordList = list(word)
        wordList[i], wordList[i+1] = wordList[i+1], wordList[i]
        match = "".join(wordList)
        if match in tokens:
            matches[match] = distance(word, match)

    if len(matches) > 0:
        return max(matches, key=matches.get), dict(sorted(matches.items(), key=lambda item: item[1]))
    else:
        return word.upper(), 'No matches!'


out = ''
prompt = ''
# start main loop
os.system('clear')
print('Welcome to russian spell checker!')
while True:
    prompt += out + ' '
    out = input(prompt + '>')
    if out == '':
        break
    out, msg = checkSpelling(out)
    os.system('clear')
    print(msg)
