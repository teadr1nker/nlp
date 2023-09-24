#!/usr/bin/python3
import io
import numpy as np


def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = []
    # print('open file')
    i = 0
    for line in fin:
        tokens = line.rstrip().split(' ')
        # data[tokens[0]] = float(tokens[1:])
        # print(f"token {tokens[0]} {i}")
        data.append(tokens[1:])
        i += 1
        if i >= 3000:
            break
    return np.array(data, np.float32)


ru = load_vectors('vectors/cc.ru.300.vec')
en = load_vectors('vectors/cc.en.300.vec')

U, S, Vh = np.linalg.svd(np.dot(en, ru.T))

W = np.dot(U, Vh)

np.save('vectors/W', W)
