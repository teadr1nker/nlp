#!/usr/bin/python
import json, os, difflib, operator
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


keyboard = [list('йцукенгшщзхъ'),
            list('фывапролджэ'),
            list(' ячсмитьбю')]

# get approx keyboard distance
def kbDistance(a, b):
    x = [0, 0]
    y = [0, 0]
    for i, letter in enumerate([a, b]):
        for j, row in enumerate(keyboard):
            if letter in row:
                x[i] = row.index(letter)
                y[i] = j
                break
            elif j == 2 and letter not in row:
                print(f'Non cyrillic charecter {letter}!')
                return 0.1

    return 1 - np.sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2) / 12.37

# read tokens
with open('words.json') as f:
    tokens = json.load(f)['words']

alphabet = 'абвгдеёжзийклмнопрстуфчцчшщъыьэюя'

# spell checker
def checkSpelling(word):
    word = word.lower()
    if word in tokens:
        return word, 'No error!'

    matches = {}

    # adding letter
    for i in range(len(word)+1):
        for letter in alphabet:
            match = word[:i] + letter + word[i:]
            if match in tokens:
                if i == 0:
                    score = kbDistance(match[i], match[i+1])
                elif i == len(match) - 1:
                    score = kbDistance(match[i], match[i-1])
                else:
                    score = max(kbDistance(match[i], match[i-1]),
                                kbDistance(match[i], match[i+1]))
                matches[match] = round(score * distance(word, match), 2)
    #removing letter
    for i in range(len(word)):
        match = word[:i] + word[i+1:]
        letter = word[i]
        if match in tokens:
            if i == 0:
                score = kbDistance(letter, match[i+1])
            elif i >= len(match) - 2:
                score = kbDistance(letter, match[i-1])
            else:
                score = max(kbDistance(letter, match[i+1]),
                            kbDistance(letter, match[i-1]))

            matches[match] = round(distance(word, match) * score, 2)
    # replace letter
    for i in range(len(word)):
        for letter in alphabet:
            match = word[:i] + letter + word[i+1:]
            if match in tokens:
                score = kbDistance(word[i], letter) * distance(word, match)
                matches[match] = round(score, 2)
    # swap two letters
    for i in range(len(word)-1):
        wordList = list(word)
        wordList[i], wordList[i+1] = wordList[i+1], wordList[i]
        match = "".join(wordList)
        if match in tokens:
            matches[match] = round(distance(word, match) * .75, 2)

    if len(matches) > 0:
        return max(matches, key=matches.get), dict(sorted(matches.items(),
                                                          key=operator.itemgetter(1),
                                                          reverse=True))
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
