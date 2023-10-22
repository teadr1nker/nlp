#!/usr/bin/python3
from gensim.models import Word2Vec

model = Word2Vec.load('mymodelFT')

print(model.wv.most_similar(positive=["Россия"]))
print(model.wv.most_similar(positive=["человек"]))
print(model.wv.doesnt_match(["кафе", "ресторан", "велосипед"]))


def test(arr):
    print(f'\npos: {arr[:-1],} neg: {arr[-1:]}')
    print(model.wv.most_similar(positive=arr[:-1],
                                negative=arr[-1:],
                                topn=5))


test(["король", "женщина", "мужчина"])
test(["программист", "музыка", "код"])
test(["сон", "испуг", "хороший"])
test(["исследования", "искусство", "наука"])
test(["Россия", "Токио", "Москва"])
test(["голова", "мозг", "волосы"])
test(["ночь", "свет", "темнота"])
test(["бекон", "пить", "есть"])
# test(['сосиска', "большая", "маленькая"])
test(["вода", "душа", "тело"])
