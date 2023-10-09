#!/usr/bin/python3
import json
import fasttext

with open('serb.txt') as f:
    serb = f.read()

modelSR = fasttext.load_model('vectors/cc.sr.300.bin')

serbWords = serb.split(' ')
sr = {word: str(list(modelSR.get_word_vector(word))) for word in serbWords}

with open('serb.json', 'w') as f:
    f.write(json.dumps(sr))



