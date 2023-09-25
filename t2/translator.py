#!/usr/bin/python3
import json


with open('dictionary.json') as f:
    dictionary = json.load(f)

while True:
    word = input('>')
    if word in dictionary:
        print(dictionary[word])
    else:
        print(f'({word})')
