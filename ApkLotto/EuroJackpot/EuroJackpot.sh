#!/bin/bash

# Pobranie linii z wylosowanymi numerami i zapisanie w pliku
wget http://www.lotto.pl/eurojackpot/wyniki-i-wygrane -q -O - | grep -n "\<div class\=\"ostatnie\-wyniki" > lottohtml

# Wydzielenie z linii najnowszych 5 wylosowanych liczb
grep -o '">[0-9]\{1,2\}' ./lottohtml | head -n7 | sed 's|[^0-9]||g' > lottonumery

data=$( grep -o '[0-9]\{1,2\}-[0-9]\{1,2\}' ./lottohtml | head -n1 )-2018
numery=$( cat ./lottonumery | head -n5 | sort -g | tr '\n' ',' )
plus=$( cat ./lottonumery | tail -n2 | sort -g | tr '\n' ' ' )

echo "${numery::-1}" > "$data"
echo "${plus::-1}" >> "$data"

# Usuwanie utworzonych plików
rm lottohtml | rm lottonumery
