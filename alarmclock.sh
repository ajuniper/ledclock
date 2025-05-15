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

amixer cset numid=1 ${volume}% >/dev/null

duration=$((duration*60))

trap 'stopping=1' TERM

function volume () {
    while [[ -z $stopping && $volume -lt ${maxvolume} && $SECONDS -lt $duration ]] ; do
        sleep ${interval}
        ((volume++))
        amixer cset numid=1 ${volume}% >/dev/null
    done
    if [[ -z $stopping && $SECONDS -lt $duration ]] ; then
        sleep $((duration - SECONDS))
    fi
    /home/pi/audio.sh stop
}

volume &
volpid=$!

failcount=0
while [[ -d /proc/$volpid ]] ; do
    SECONDS=0
    if ! /home/pi/audio.sh -f radio "$station" || [[ $SECONDS -lt 10 ]] ; then
        # radio is failing very quickly
        # if too many tries then try a different one
        if [[ $((++failcount)) -gt 5 ]] ; then
            station=radio2
        fi
        # back off a bit
        /home/pi/audio.sh stop
        sleep 10
    fi
done
kill $volpid
wait $volpid
