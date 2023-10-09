#!/usr/bin/python3
import json
import fasttext

with open('rus2.txt') as f:
    rus = f.read()

modelRU = fasttext.load_model('vectors/cc.ru.300.bin')

rusWords = rus.split('\n')
ru = {word: str(list(modelRU.get_word_vector(word))) for word in rusWords}

with open('rus.json', 'w') as f:
    f.write(json.dumps(ru))
