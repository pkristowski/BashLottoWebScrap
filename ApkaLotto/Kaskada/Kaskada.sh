#!/bin/bash

# Pobranie linii z wylosowanymi numerami i zapisanie w pliku
wget http://www.lotto.pl/kaskada/wyniki-i-wygrane -q -O - | grep -n "\<div class\=\"ostatnie\-wyniki" > lottohtml

# Wydzielenie z linii najnowszych 12 wylosowanych liczb i posortowanie ich
grep -o '">[0-9]\{1,2\}' ./lottohtml | head -n12 | sed 's|[^0-9]||g' | sort -g > lottonumery

# dzien-miesiac-rok, dzien tygodnia, godzina
data=$( grep -o '[0-9]\{1,2\}-[0-9]\{1,2\}' ./lottohtml | head -n1 )-2018
numery=$( cat ./lottonumery | tr '\n' ',' | tr '\t' ',' )

if [ -e ./$data ] ; then

        cat ./$data > temp
        echo "$numery" > "$data"
        cat ./temp >> "$data"
else
        echo "$numery" > "$data"
fi

# Usuwanie utworzonych plików
rm lottohtml | rm lottonumery | rm temp
