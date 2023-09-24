#!/usr/bin/python3
import io
import numpy as np
from scipy import spatial

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = []
    words = []
    # print('open file')
    i = 0
    for line in fin:
        tokens = line.rstrip().split(' ')
        # data[tokens[0]] = float(tokens[1:])
        # print(f"token {tokens[0]} {i}")
        words.append(tokens[0])
        data.append(tokens[1:])
        i += 1
        if i >= 3000:
            break
    return words, np.array(data, np.float32)


tokensRu, ru = load_vectors('vectors/cc.ru.300.vec')
tokensEn, en = load_vectors('vectors/cc.en.300.vec')

W = np.load('vectors/W.npy')
P = np.dot(W, ru)
enTree = spatial.KDTree(en)


# print(ru[tokensRu.index(tokensRu[100])], tokensRu[100])
def translate(wordRu):
    if wordRu not in tokensRu:
        return f'({wordRu})'
    vectRu = P[tokensRu.index(wordRu)]
    closest = enTree.query(vectRu)
    return tokensEn[closest[1]]

print(translate('еще'))

