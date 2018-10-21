#!/bin/bash

# Pobranie linii z wylosowanymi numerami i zapisanie w pliku
wget http://www.lotto.pl/mini-lotto/wyniki-i-wygrane -q -O - | grep -n "\<div class\=\"ostatnie\-wyniki" > lottohtml

data=$( grep -o '[0-9]\{1,2\}-[0-9]\{1,2\}' ./lottohtml | head -n1 )-2018
wynik=$( grep -o 'wynik_mini-lotto">[0-9]\{1,2\}' ./lottohtml | head -n5 | sed 's|[^0-9]||g' | sort -g | tr '\n' ',' )

echo "${wynik::-1}" > "$data"

# Usuwanie utworzonych plików
rm lottohtml
