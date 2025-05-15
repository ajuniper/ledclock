#!/bin/bash
pin=4
gap=120
# p1=buttons
function tx ()
{
	while ! sudo timeout 3 /home/pi/irsling -p $pin -f /home/pi/jedi_new.conf -- $1 ; do
            sleep 3
        done
	sleep ${2:-$gap}
	#sleep 5
}

if [[ $1 = start ]] ; then
    tx "1 1 yellow - - - -"
    tx +
    tx +
    tx +
    tx +
    tx white 1
else
    tx "0 0 0"
fi
