#!/usr/bin/python3
import numpy as np

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def oneHotEncodingRus(word, size):
    n = len(alphabet)
    m = len(word)
    offset = size - m
    ohe = np.zeros((size, n))
    for i in range(m):
        letter = word[i].lower()
        if letter in alphabet:
            ohe[i + offset, alphabet.index(letter)] = 1
    return ohe


if __name__ == '__main__':
    print(oneHotEncodingRus('тест', 6))

