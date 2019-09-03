#!/bin/bash

# starting volume
volume=${volume:-70}
# minutes on
time=${time:-60}
# seconds between increments
interval=${interval:-30}
# radio stream = radio4
stream="${stream:-http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_fourfm/format/pls.pls}"

radio() {
    while true ; do
        mplayer -nocache -playlist "$stream"
    done
}


amixer cset numid=3 1
amixer cset numid=1 ${volume}%

time=$((time*60))
radio &
radio=$!

finished() {
    kill $radio
    killall mplayer
    wait
}
trap finished EXIT

while [[ $volume -lt 99 && $SECONDS -lt $time ]] ; do
    sleep ${interval}
    ((volume++))
    amixer cset numid=1 ${volume}%
done
if [[ $SECONDS -lt $time ]] ; then
    sleep $((time - SECONDS))
fi
