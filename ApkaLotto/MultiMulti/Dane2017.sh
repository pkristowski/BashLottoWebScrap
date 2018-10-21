#!/bin/bash

# Pobranie linii z wylosowanymi numerami i zapisanie w pliku
wget http://megalotto.pl/wyniki/multi-multi/losowania-z-roku-2017 -q -O - | sed -n -e '/lista_ostatnich_losowan"/,$p'  > lottohtml

# tworzenie pliku z numerami
grep -o '>[0-9]\{1,2\}\s\{0,1\}<' ./lottohtml | sed 's|[^0-9]||g' | tr '\n' ',' | tr ' ' ',' | xargs -n 20 -d, > lottonumery
grep -o 'plus"\s\{0,1\}.\{0,27\}>[0-9]\{1,2\}' ./lottohtml | grep -o '>[0-9]\{1,2\}' | sed 's|[^0-9]||g' > lottoplus

# tworzenie pliku z datami
grep -o '>[0-9]\{1,2\}-[0-9]\{1,2\}-2017' ./lottohtml | tr -d '>' > lottodaty

# tworzenie plikow o nazwie DATA z zawartoscia NUMERY
liczba=$( wc -l ./lottonumery | sed 's|[^0-9]||g' )
i=1

#tworzenie plikow po liniach z dat
cat ./lottodaty | xargs touch --

while [ "$i" -le "$liczba" ] ; do

data=$( sed "$i q;d" ./lottodaty )

sed "$i q;d" ./lottonumery >> "$data"
sed "$i q;d" ./lottoplus >> "$data"

i=$((i+1))

done

# Usuwanie utworzonych plików
rm lotto* | find . -size 0 -delete
