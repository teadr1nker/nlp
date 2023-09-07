#!/usr/bin/bash

mkdir texts
cd texts

books=('CrimeAndPunishment' 'EugeneOnegin' 'FathersAndSons' 'MasterAndMargarita' 'WarAndPeace')

for book in "${books[@]}"
do
    wget "https://github.com/nevmenandr/word2vec-russian-novels/raw/master/books_before/$book.txt"
done
