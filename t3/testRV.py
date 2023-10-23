#!/usr/bin/python3
import gensim

stream = open('vectors/model.txt', 'r')

model = gensim.models.KeyedVectors.load_word2vec_format('vectors/model.bin',
                                                        binary=True)
print('Loaded model')

print(model.most_similar('россия_PROPN'))
print(model.most_similar(positive=["человек_NOUN"]))
print(model.doesnt_match(["кафе_NOUN", "ресторан_NOUN", "велосипед_NOUN"]))


def test(arr):
    print(f'\npos: {arr[:-1],} neg: {arr[-1:]}')
    print(model.most_similar(positive=arr[:-1],
                             negative=arr[-1:],
                             topn=5))


test(["король_NOUN", "женщина_NOUN", "мужчина_NOUN"])
test(["программист_NOUN", "музыка_NOUN", "код_NOUN"])
test(["сон_NOUN", "испуг_NOUN", "хороший_ADJ"])
test(["исследование_NOUN", "искусство_NOUN", "наука_NOUN"])
test(["россия_PROPN", "токио_PROPN", "москва_PROPN"])
test(["голова_NOUN", "мозг_NOUN", "волос_NOUN"])
test(["ночь_NOUN", "свет_NOUN", "темнота_NOUN"])
test(["бекон_NOUN", "пить_NOUN", "есть_NOUN"])
test(['сосиска_NOUN', "большой_ADJ", "маленькая_ADJ"])
test(["вода_NOUN", "душа_NOUN", "тело_NOUN"])
