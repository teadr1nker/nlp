#!/usr/bin/python3
import os, re, nltk, json

nltk.download('punkt')
path = 'texts/'
bigText = ''

# read all the files
for book in os.listdir(path):
    with open(path + book, "r") as f:
        bigText += f.read() + ' '

# tokenize text
tokens = [nltk.word_tokenize(t) for t in nltk.sent_tokenize(bigText)]
filtetedTokens = []
r = re.compile("[а-яА-Я]+")

# filter tokens only for cyrillic words
for token in tokens:
    filtetedTokens += [w.lower() for w in filter(r.match, token)]

# print(set(filtetedTokens))

# leave only unique words
filtetedTokens = list(set(filtetedTokens))

# save tokens as json
with open('words.json', 'w') as f:
    f.write(json.dumps({'words': filtetedTokens}))
