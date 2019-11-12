#!/bin/bash
pin=23
gap=120
# p1=buttons
function tx ()
{
	sudo /home/pi/irsling -p $pin -f /home/pi/jedi_new.conf -- $1
	sleep ${2:-$gap}
}

tx "1 yellow - - - -"
tx +
tx +
tx +
tx +
tx white 300
tx "0 0 0"
