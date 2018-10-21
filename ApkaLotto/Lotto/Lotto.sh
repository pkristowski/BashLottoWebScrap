#!/bin/bash

# Pobranie linii z wylosowanymi numerami i zapisanie w pliku
wget http://www.lotto.pl/lotto/wyniki-i-wygrane -q -O - | grep -n "ostatnie-wyniki" > lottohtml

data=$( grep -o '[0-9]\{1,2\}-[0-9]\{1,2\}' ./lottohtml | head -n1 )
liczby=$( grep -o '">[0-9]\{1,2\}<' ./lottohtml | head -n6 | sed 's|[^0-9]||g' | tr '\n' ',' )

echo "${liczby::-1}" > "$data"-2018

# Usuwanie utworzonych plików
# rm lottohtml
