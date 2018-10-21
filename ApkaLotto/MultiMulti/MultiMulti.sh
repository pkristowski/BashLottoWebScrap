#!/bin/bash

# Pobranie linii z wylosowanymi numerami i zapisanie w pliku
wget http://www.lotto.pl/multi-multi/wyniki-i-wygrane -q -O - | grep -n "\<div class\=\"ostatnie\-wyniki" > lottohtml

# Wydzielenie z linii najnowszych 20 wylosowanych liczb i posortowanie ich
grep -o '">[0-9]\{1,2\}' ./lottohtml | head -n20 | sed 's|[^0-9]||g' | sort -g > lottonumery

#dzien-miesiac-rok, dzien tygodnia, godzina
data=$( grep -o '[0-9]\{1,2\}-[0-9]\{1,2\}' ./lottohtml | head -n1 )-2018
numery=$( cat ./lottonumery | tr '\n' ' ' | tr '\t' ',' )
plus=$( grep -o 'plus">[0-9]\{1,2\}' ./lottohtml | head -n1 | sed 's|[^0-9]||g' )

if [ -e ./$data ] ; then

	cat ./$data > temp
	echo "$numery" > "$data"
	echo " " >> "$data"
	echo "$plus" >> "$data"
	cat ./temp >> "$data"
else
	echo "$numery" > "$data"
	echo " " >> "$data"
        echo "$plus" >> "$data"
fi

# Usuwanie utworzonych plików
rm lotto* | rm temp
