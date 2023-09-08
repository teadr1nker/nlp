#!/usr/bin/python
import json, os

# read tokens
with open('words.json') as f:
    tokens = json.load(f)['words']

# print(tokens)
alphabet = 'абвгдеёжзийклмнопрстуфчцчшщъыьэюя'

# spell checker
def checkSpelling(word):
    word = word.lower()
    if word in tokens:
        return word, 'No error!'

    matches = []

    #adding letter
    for i in range(len(word)+1):
        for letter in alphabet:
            match = word[:i] + letter + word[i:]
            if match in tokens:
                matches.append(match)
    #removing letter
    for i in range(len(word)):
        match = word[:i] + word[i+1:]
        if match in tokens:
            matches.append(match)
    #replace letter
    for i in range(len(word)):
        for letter in alphabet:
            match = word[:i] + letter + word[i+1:]
            if match in tokens:
                matches.append(match)
    #swap two letters
    for i in range(len(word)-1):
        wordList = list(word)
        wordList[i], wordList[i+1] = wordList[i+1], wordList[i]
        match = "".join(wordList)
        if match in tokens:
            matches.append(match)
    if len(matches) > 0:
        return matches[0], matches
    else:
        return word.upper(), 'No matches!'


out = ''
prompt = ''
# start main loop
os.system('clear')
print('Welcome to russian spell checker!')
while True:
    prompt += out + ' '
    out = input(prompt + '>')
    if out == '':
        break
    out, msg = checkSpelling(out)
    os.system('clear')
    print(msg)
