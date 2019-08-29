#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import RPi.GPIO as GPIO
from inotify_simple import INotify, flags

pin = 12
pin_on=GPIO.HIGH
pin_off=GPIO.LOW
#pin_on=GPIO.LOW
#pin_off=GPIO.HIGH
# min ms that amp is on for
min_on_time = 3000
# how long to wait from close to amp off
delayed_off = 0
# how long to wait from open to amp on
delayed_on = 0

count = 0
ontime = 0
pinstate = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT, initial=pin_off)

inotify = INotify()
inotify.add_watch("/dev/snd/pcmC0D0p", flags.OPEN|flags.CLOSE_WRITE|flags.CLOSE_NOWRITE);
# TODO use wildcard
#inotify.add_watch("/dev/snd/pcmC0D1p", flags.OPEN|flags.CLOSE_WRITE|flags.CLOSE_NOWRITE);

def turnoff():
    #print("all done")
    GPIO.output(pin, pin_off)
    GPIO.cleanup()

import atexit
atexit.register(turnoff)

#print("ready...")

current_milli_time = lambda: int(round(time.time() * 1000))

events=[]
while (True):
    if (len(events) == 0):
        # calculate the timeout
        readtime = -1
        if (delayed_off > 0):
            readtime =  delayed_off - current_milli_time()
        #print("wait for up to %d for events"%(readtime))
        events = inotify.read(readtime)
        #print("got %d events"%(len(events)))

    if ((len(events) == 0) and (delayed_off > 0)):
        # delayed off
        #print("delayed off")
        GPIO.output(pin, pin_off)
        pinstate = 0

    # to get here we have any delayed off gets cancelled
    delayed_off = 0

    while (len(events) > 0):
        event=events[0]
        events.pop(0)
        #print(event)
        for flag in flags.from_mask(event.mask):
            if (flag == flags.OPEN):
                count+=1
                #print("OPEN, count now %d"%(count))
                if (count == 1):
                    if (pinstate == 0):
                        pinstate = 1
                        ontime = current_milli_time()
                        if (delayed_on > 0):
                            time.sleep(delayed_on/1000.0)
                        GPIO.output(pin, pin_on)
                        #print("pin on")
                    else:
                        #print("pin already on")
                        pass
            else:
                count-=1
                #print("CLOSE, count now %d"%(count))
                if (count == 0):
                    # want to turn off - have we been on long enough?
                    if (len(events) > 0):
                        # some events are already pending skip the off
                        #print("already have %d pending events"%(len(events)))
                        pass

                    elif ((current_milli_time() - ontime) < min_on_time):
                        # not on long enough, more events pending?
                        #print("not been on long enough")

                        # wait a while - min wait time beyond the on
                        delayed_off = min_on_time + ontime

                    else:
                        # turn off after a short wait in case of another event
                        #print("pin off")
                        delayed_off = 50 + current_milli_time()
