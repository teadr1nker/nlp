#!/usr/bin/python3
import io
import numpy as np
from scipy import spatial
import re
import json


def load_vectors(fname, limit):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = []
    words = []
    # print('open file')
    i = 0
    for line in fin:
        tokens = line.rstrip().split(' ')
        x = re.search('[A-zА-я]', tokens[0])
        if x:
            # data[tokens[0]] = float(tokens[1:])
            # print(f"token {tokens[0]} {i}")
            # print(f'found word {tokens[0]}')
            words.append(tokens[0])
            data.append(tokens[1:])
            i += 1
        # else:
        #     print(f'not word {tokens[0]}')
        if i >= limit:
            break
    return words, np.array(data, np.float32)


limit = 1000
tokensRu, ru = load_vectors('vectors/cc.ru.300.vec', limit)
tokensEn, en = load_vectors('vectors/cc.en.300.vec', limit)

U, S, Vh = np.linalg.svd(np.dot(en, ru.T))

W = np.dot(U, Vh)

P = np.dot(W, ru)

enTree = spatial.KDTree(en)
dictionary = {}

print(test2)
for i in range(limit):
    wordRu = tokensRu[i]
    # closest = enTree.query(P[i])
    wordEn = tokensEn[np.where(test2 == i)]
    # print(closest[1], i)
    dictionary[wordRu] = wordEn

with open('dictionary.json', 'w') as f:
    f.write(json.dumps(dictionary))
