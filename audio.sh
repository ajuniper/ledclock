#!/bin/bash
# script to play audio in background
# p1=command: stop/say/radio/url/local
# p2=id (words, radioname, url, path)

# -f to run in foreground
if [[ $1 = -f ]] ; then
    NODISOWN=1
    shift
fi

cmd="$1"
id="$2"
extra="$3"

if ! [[ $cmd = +(stop|say|radio|url|local) ]] ; then
    echo "Invalid command $cmd"
    exit 1
fi

if [[ -z $id && $cmd != stop ]] ; then
    echo "id not specified"
    exit 1
fi

declare -A radio
radio[jackfm]='http://listen-jackmedia.sharp-stream.com/390_jack_fm_128_mp3'
radio[jack2]='http://listen-jackmedia.sharp-stream.com/390_jack_2_128_mp3'
radio[radio1]='http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_one/format/pls.pls'
radio[radio2]='http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_two/format/pls.pls'
radio[radio3]='http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_three/format/pls.pls'
radio[radio4]='http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_fourfm/format/pls.pls'
radio[kiss_es]='http://kissfm.kissfmradio.cires21.com/kissfm.mp3'

if [[ $cmd = radio && ${radio[$id]} = "" ]] ; then
    echo "radio $id unknown"
    exit 1
fi

if [[ $PPID != 1 && -z $NODISOWN ]] ; then
    nohup $0 "$@" </dev/null >/dev/null 2>&1 &
    disown
    exit
fi

#rundir=${rundir:-${XDG_RUNTIME_DIR:-/run/user/1000}}
rundir=/tmp
runfile=$rundir/audio.run
lckfile=$rundir/audio.lck
touch $lckfile
chmod 666 $lckfile
(
    shopt -s extglob
    function alldone() {
        [[ -n $newpid ]] && {
            wait $newpid
            # only tidy if it was our log file
            [[ -z $NOKILL ]] && rm -f $runfile
        }
    }
    trap alldone EXIT
    function stopnow() {
        [[ -n $newpid ]] && kill -s $1 $newpid
    }
    trap 'stopnow TERM' TERM
    trap 'stopnow TERM' INT
    trap 'stopnow HUP' HUP

    flock 3

    # kill pre-existing
    [[ -z $NOKILL ]] && oldpid=$(head -1 $runfile 2>/dev/null)
    if [[ -n $oldpid ]] ; then
        kill -s TERM $oldpid
        while [[ -n $oldpid && -d /proc/$oldpid && $SECONDS -lt 10 ]] ; do
            sleep 1
        done
        if [[ -d /proc/$oldpid ]] ; then
            killall -s TERM -$oldpid
            sleep 1
            kill -s KILL -$oldpid
            killall -s TERM -q mpg123 play
            sleep 1
            killall -s KILL -q mpg123 play
            sleep 1
        fi

        [[ $cmd = stop ]] && exit
    fi

    # remember that I am running
    [[ -z $NOKILL ]] && {
        echo -e "$BASHPID\n$id" >$runfile
        chmod 666 $runfile
    }

    case $cmd in
        say)
            IFS="#" read -a ii <<<"${id//    /#}"
            for i in "${ii[@]}" ; do
                # unwanted characters, fold spaces
                i="${i//[^-[:alnum:] +.%$£&\!]/}"
                i="${i//+( )/ }"
                # url escaping
                i="${i//+/%2B}"
                i="${i//&/%26}"
                i="${i// /+}"
                mpg123 -q --no-control "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=${i}&tl=${extra:-en}" >>$runfile 2>&1
                #newpid=$!
            done
            ;;
        url)
            if [[ $id = *.pls ]] ; then
                mpg123 -q --no-control -@ "$id" >>$runfile 2>&1 &
            elif [[ $id = *.mp3 ]] ; then
                curl -s "$id" >/tmp/$$.mp3
                mpg123 -q --no-control "/tmp/$$.mp3" >>$runfile 2>&1 &
                rm -f /tmp/$$.mp3
            else
                #mpg123 -q --no-control "$id" >>$runfile 2>&1 &
                f="/tmp/${id##*/}"
                curl -s "$id" >"$f"
                aplay "$f"
                rm -f "$f"
            fi
            newpid=$!
            ;;
        local)
            play -q "$id" >>$runfile 2>&1 &
            newpid=$!
            ;;
        radio)
            r="${radio[$id]}"
            mpg123 -q --no-control -@ "$r" >>$runfile 2>&1 &
            newpid=$!
            ;;
    esac

    if [[ -n $newpid ]] ; then
        # if we have something to wait for
        # remember it, then wait for it to finish
        flock -u 3
        wait $newpid
    fi
) 3<$lckfile
