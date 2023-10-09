#!/usr/bin/python3
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def fix(strlist):
    strlist = strlist.replace('[', '')
    strlist = strlist.replace(']', '')

    return [float(x) for x in strlist.split(', ')]


with open('bel.json') as f:
    bel = json.load(f)

with open('rus.json') as f:
    rus = json.load(f)

size = min(len(bel), len(rus))

print(f'dataset size: {size}')

ruWords = [key for key in rus]
beWords = [key for key in bel]

R = np.array([fix(rus[key]) for key in rus], np.float32)[:size]
P = np.array([fix(bel[key]) for key in bel], np.float32)[:size]

U, S, Vh = np.linalg.svd(np.dot(P.T, R))
W = np.dot(U, Vh)

dictionary = {}

for i in range(size):
    word = ruWords[i]
    ruVec = R[i]
    ruVec = np.dot(W, ruVec)

    similarities = cosine_similarity(ruVec.reshape(1, -1), P)
    similar = np.argmax(similarities)
    dictionary[word.lower()] = beWords[similar].lower()

    print(i, similar)

with open('dictionary.json', 'w') as f:
    f.write(json.dumps(dictionary))

