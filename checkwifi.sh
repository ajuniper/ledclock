#!/bin/bash
# many commands are in sbin
PATH=$PATH:/sbin

# interface of interest
i=wlan0

# where we log to
l=/var/log/checkwifi

# default limit
t=300

# wait for 5 minutes of uptime
awk "(\$1<$t){e=1}END{exit e}" /proc/uptime || exit 0

# ping router
r=$(route -n | awk '($1=="0.0.0.0"){print $2}')
[[ $r != 0.0.0.0 ]] && ping -W 3 -c 3 $r >/dev/null 2>&1 && exit 0

# check >5 mins since last bounce if invoked from cron
[[ -z $FORCE ]] &&
    [[ -n $(find ${l%/*} -name "${l##*/}*" -and -mmin -$(((t+59)/60)) 2>/dev/null) ]] && exit 0

# decide what action
FORCE=${FORCE:-5}
d=$l.$FORCE.$(date +%s)

# do stuff and log it
(
    set -x
    date
    ip a s
    { echo -e "status\nsignal_poll\nscan" ; sleep 3 ; echo "scan_result" ; } | wpa_cli -i $i

    #systemctl status
    #systemctl status networking.service
    #systemctl status dhcpcd.service
    journalctl -u dhcpcd
    journalctl -u networking

    # take more and more drastic action
    case $FORCE in
        1)  # reattempt association
            wpa_cli -i $i reassociate
            ;;
        2)  # disconnect / reconnect
            wpa_cli -i $i disconnect
            sleep 5
            wpa_cli -i $i scan
            sleep 5
            wpa_cli -i $i scan_results
            wpa_cli -i $i reconnect
            ;;
        3)  # full down/up
            ifdown $i
            sleep 5
            ifup $i
            ;;
        4)  # restart dhcpcd
            systemctl restart dhcpcd.service
            ;;
        *)  # restart entire networking
            systemctl restart networking.service
            ;;
    esac

    echo "FORCE=$((FORCE+1)) $0" | at -M now+1min
) >/tmp/checkwifi.txt 2>&1

# only keep pass 1-5, after that things are stuck and go on forever
if [[ $FORCE -le 8 ]] ; then
    cat /tmp/cw.txt /tmp/checkwifi.txt >$d
    rm -f /tmp/checkwifi.txt
    sync
else
    rm /tmp/checkwifi.txt
fi

# only keep the most recent 100
ls -t $l* | tail -n +102 | xargs -r rm -f
