#!/usr/bin/python3
import json
import numpy as np
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity


def fix(strlist):
    strlist = strlist.replace('[', '')
    strlist = strlist.replace(']', '')

    return [float(x) for x in strlist.split(', ')]


with open('bel.json') as f:
    bel = json.load(f)

with open('rus.json') as f:
    rus = json.load(f)

with open('bel2.txt') as f:
    belList = f.read().split('\n')

with open('rus2.txt') as f:
    rusList = f.read().split('\n')

ruWords = []
beWords = []
P = []
R = []
for i in range(min(len(belList), len(rusList))):
    r = rusList[i]
    b = belList[i]
    # print(r, b)
    if r in rus and b in bel:
        ruWords.append(r)
        beWords.append(b)
        R.append(fix(rus[r]))
        P.append(fix(bel[b]))

P = np.array(P)
R = np.array(R)

print(f'dataset size: {len(beWords)} {len(ruWords)}')

print(R.shape, P.shape)
U, S, Vh = np.linalg.svd(np.dot(P.T, R))
W = np.dot(U, Vh)

print(f'W shape {W.shape}')
dictionary = {}
tree = spatial.KDTree(P)

for i in range(len(ruWords)):
    word = ruWords[i]
    ruVec = R[i]
    ruVec = np.dot(W, ruVec)

    similarities = cosine_similarity(ruVec.reshape(1, -1), P)
    similar = np.argmax(similarities)

    dictionary[word.lower()] = beWords[similar].lower()

with open('dictionary.json', 'w') as f:
    f.write(json.dumps(dictionary))
