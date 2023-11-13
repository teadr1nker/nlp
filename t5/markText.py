#!/usr/bin/python3
import numpy as np
import nltk
import os
import re
import pymorphy2
import json
nltk.download('punkt')

bigText = ''
path = '../t1/texts/'
for book in os.listdir(path):
    with open(path + book, "r") as f:
        bigText += f.read() + ' '

sentences = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(bigText)]

r = re.compile("[а-яА-Я]+")

filteredSentences = []

# filter tokens only for cyrillic words
for sentence in sentences:
    filteredSentences.append([w.lower() for w in filter(r.match, sentence)])

dictionary = {'sentences': [], 'tags': []}

morph = pymorphy2.MorphAnalyzer()

for sentence in filteredSentences:
    dictionary['sentences'].append(sentence)
    tags = []
    for word in sentence:
        tags.append(morph.parse(word)[0].tag.POS)
    dictionary['tags'].append(tags)


with open('train.json', 'w') as f:
    f.write(json.dumps(dictionary))
