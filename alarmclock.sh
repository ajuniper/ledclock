#!/bin/bash
# p1=station
# p2=duration

# station
station="$1"

# starting volume
volume=${volume:-1}
maxvolume=${maxvolume:-55}

# minutes on
duration=${2:-45}

# seconds to max volume if unspecified
durationtomax=${durationtomax:-600}

# seconds between increments
interval=${interval:-$(( durationtomax / (maxvolume-volume) ))}

PATH=${PATH}:$(dirname $(readlink -f $0))

timetostop() {
    stopping=1
    ./audio.sh stop
}

radio() {
    trap timetostop TERM
    while [[ -z $stopping ]] ; do
        ./audio.sh -f radio "$station"
    done
}


amixer cset numid=1 ${volume}% >/dev/null

duration=$((duration*60))
radio &
radio=$!

finished() {
    stopping=1
    kill $radio
    wait
}
trap finished EXIT
trap 'stopping=1' TERM

while [[ -z $stopping && $volume -lt ${maxvolume} && $SECONDS -lt $duration ]] ; do
    sleep ${interval}
    ((volume++))
    amixer cset numid=1 ${volume}% >/dev/null
done
if [[ -z $stopping && $SECONDS -lt $duration ]] ; then
    sleep $((duration - SECONDS))
fi
