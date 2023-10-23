#!/usr/bin/python3
import fasttext

model = fasttext.load_model('../t2/vectors/cc.ru.300.bin')

print(model.get_nearest_neighbors('Россия'))
def test(arr):
    print(f'\npos: {arr[:-1],} neg: {arr[-1:]}')
    print(model.get_analogies(arr[0], arr[2], arr[1]))

test(["король", "женщина", "мужчина"])
test(["программист", "музыка", "код"])
test(["сон", "испуг", "хороший"])
test(["исследования", "искусство", "наука"])
test(["Россия", "Токио", "Москва"])
test(["голова", "мозг", "волосы"])
test(["ночь", "свет", "темнота"])
test(["бекон", "пить", "есть"])
test(['сосиска', "большая", "маленькая"])
test(["вода", "душа", "тело"])
