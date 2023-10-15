#!/usr/bin/python3
import json
import fasttext

with open('bel2.txt') as f:
    bel = f.read()

modelBE = fasttext.load_model('vectors/cc.be.300.bin')

belWords = bel.split('\n')
be = {word: str(list(modelBE.get_word_vector(word))) for word in belWords}

with open('bel.json', 'w') as f:
    f.write(json.dumps(be))


