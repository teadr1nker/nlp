#!/usr/bin/python3
from gensim.models import Word2Vec
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

model = Word2Vec(min_count=10,      # минимальная частота слова (2-100)
                 window=3,          # длина окна (2-10)
                 vector_size=100,          # размер эмбеддинга (50-300)
                 sample=3e-5,       #
                 alpha=0.03,        # learning rate
                 min_alpha=0.0007,  #
                 negative=20)
print(f'Building vocab {datetime.now()}')

model.build_vocab(sentences, progress_per=10000)

print(f'Training Model {datetime.now()}')
model.train(sentences, total_examples=model.corpus_count,
            epochs=2, report_delay=1)

model.init_sims(replace=True)

print(model.wv.most_similar(positive=["России"]))
print(model.wv.doesnt_match(["кафе", "ресторан", "велосипед"]))

model.save('mymodel')
