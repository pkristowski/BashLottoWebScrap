#!/bin/bash
CONN=$(nmcli radio wifi | wc -c)
ENAB=$(echo "enabled" | wc -c)

if [ $CONN != $ENAB ]

then

echo "Already disconnected";

elif [ -d ~/.mozilla/firefox/*.default/cookies.sqlite ]

then

rm ~/.mozilla/firefox/*.default/cookies.sqlite;
nmcli radio wifi off;
echo "WiFi disabled, cookies removed";

else

nmcli radio wifi off;
echo "WiFi disabled";

fi
