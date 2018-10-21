#!/bin/bash

# tworzenie plikow o nazwie DATA z zawartoscia NUMERY
liczba=$( wc -l ./lottonumery | sed 's|[^0-9]||g' )
i=1
#tworzenie plikow po liniach z dat
cat ./lottodaty | xargs touch --

while [ "$i" -le "$liczba" ] ; do

data=$( sed "$i q;d" ./lottodaty )
sed "$i q;d" ./lottonumery > "$data"

i=$((i+1))

done
