#!/usr/bin/python3
import json
import fasttext
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def fix(strlist):
    strlist = strlist.replace('[', '')
    strlist = strlist.replace(']', '')

    return [float(x) for x in strlist.split(', ')]


with open('serb.json') as f:
    serb = json.load(f)

with open('rus.json') as f:
    rus = json.load(f)

size = min(len(serb), len(rus))

ruWords = [key for key in rus]
srWords = [key for key in serb]

R = np.array([fix(rus[key]) for key in rus], np.float32)[:size]
P = np.array([fix(serb[key]) for key in serb], np.float32)[:size]

U, S, Vh = np.linalg.svd(np.dot(P.T, R))
W = np.dot(U, Vh)

dictionary = {}

for i in range(size):
    word = ruWords[i]
    ruVec = R[i]
    ruVec = np.dot(W, ruVec)

    similarities = cosine_similarity(ruVec.reshape(1, -1), P)
    similar = np.argmax(similarities)
    dictionary[word.lower()] = srWords[similar].lower()

    print(i, similar)

with open('dictionary.json', 'w') as f:
    f.write(json.dumps(dictionary))

