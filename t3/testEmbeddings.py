#!/usr/bin/python3
from gensim.models import Word2Vec
from datetime import datetime

model = Word2Vec.load('mymodel')

print(model.wv.most_similar(positive=["Россия"]))
print(model.wv.most_similar(positive=["человек"]))
print(model.wv.doesnt_match(["кафе", "ресторан", "велосипед"]))
print(model.wv.most_similar(positive=["король", "женщина"], negative=["мужчина"], topn=5))
print(model.wv.most_similar(positive=["программист", "музыка"], negative=["код"], topn=5))
# print(model.wv.most_similar(positive=["аналогия", "сумасшедший "], negative=["действительный"], topn=5))
print(model.wv.most_similar(positive=["сон", "испуг"], negative=["хороший"], topn=5))
print(model.wv.most_similar(positive=["исследования", "искусство"], negative=["наука"], topn=5))
print(model.wv.most_similar(positive=["сон", "испуг"], negative=["хороший"], topn=5))
print(model.wv.most_similar(positive=["Россия", "Токио"], negative=["Москва"], topn=5))
