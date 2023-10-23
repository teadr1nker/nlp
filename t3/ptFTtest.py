#!/usr/bin/python3
from gensim.models import FastText

model = FastText.load_fasttext_format('../t2/vectors/cc.ru.300.bin')
