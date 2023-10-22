#!/usr/bin/python3
from gensim.models import FastText
from datetime import datetime
import logging
import nltk
nltk.download('punkt')

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)

print(f'Reading dataset {datetime.now()}')
with open('bigText.txt', 'r') as f:
    text = f.read()

print(f'Tokenizing! {datetime.now()}')
sentences = [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text)]

del text
print(f'Creating model {datetime.now()}')
model = FastText(vector_size=100, window=3)
print(f'Bulding vocab {datetime.now()}')
model.build_vocab(corpus_iterable=sentences)

examplesCount = len(sentences)
wordsCount = model.sorted_vocab
print(f'{examplesCount} sentences')
print(f'{wordsCount} words!')

print(f'Training model {datetime.now()}')
model.train(corpus_iterable=sentences, epochs=2,
            total_examples=examplesCount, total_words=wordsCount)
print(f'Saving model {datetime.now()}')
model.save('mymodelFT')
