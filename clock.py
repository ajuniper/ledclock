#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python clock.py --cascaded 4 --block-orientation -90 --rotate 2

import re
import time
import argparse
import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

import os
import signal
import errno
from inotify_simple import INotify, flags

from PIL import ImageFont
# ok but do not like dot/slash in 0
#font = ImageFont.truetype("ProggyTiny.ttf", 16, encoding="unic")
#font = ImageFont.truetype("ProggyTinySZ.ttf", 16, encoding="unic")
# https://fonts2u.com/mono-07-55.font
font = ImageFont.truetype("/home/pi/mono/mono0755.ttf", 8, encoding="unic")
# font is 6 wide
fw=6
x=1
y=-4
stopnow=0
maxwidth=500


def clock():
    # state for deciding whether to cycle process
    state=-1

    lastmsg = ""
    tickspeed=5
    tickcount=5
    events=[]

    path="/run/clockmsg"
    if (os.getuid() != 0):
        path=("/run/user/%d/clockmsg" % os.getuid())

    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

    os.chmod(path,0o777)
    inotify = INotify()
    monitor = inotify.add_watch(path, flags.CLOSE_WRITE)

    while (stopnow == 0):
        d = datetime.datetime.now()
        msg = d.strftime("%H")
        if (d.second % 2):
            msg += ":"
        else:
            msg += " "
        msg += d.strftime("%M")
        if (msg != lastmsg):
            lastmsg = msg
            with canvas(virtual) as draw:
                draw.text((x,y),msg, font=font, fill="white")

        time.sleep(1.0/tickspeed)

        # consider whether to exit to cycle process
        if (state == -1):
            # first time thru
            state = d.hour
        elif (state != d.hour):
            # hour has moved on, we are good to exit at 3am
            state = -2
        elif (state == -2) and (d.hour == 3):
            # time to exit
            return

        # decide whether to show a message

        if (tickcount > 0):
            tickcount = tickcount - 1

        if (tickcount > 0):
            continue

        if (len(events) == 0):
            events = inotify.read(1)

        if (len(events) > 0):
            msgfile=("%s/%s" % (path,events[0].name))
            events.pop(0)
            with open(msgfile, 'r') as myfile:
                msg=myfile.read(maxwidth).replace('\n', ' ')
            os.remove(msgfile)
            showmsg(msg)
            tickcount = 5*tickspeed
            continue

        continue

        # show and scroll time
        msg = d.strftime("%A, %B %d")
        showmsg(msg)
        tickcount = 10*tickspeed


# scroll a message
def showmsg(msg, speed=20):
    lastmsg = msg
    with canvas(virtual) as draw:
        draw.text((x,y),msg, font=font, fill="white")
    time.sleep(0.5)
    for i in range(fw*len(msg)):
        virtual.set_position((i, 0))
        time.sleep(1.0/speed)
    # clear the canvas before returning
    with canvas(virtual) as draw:
        draw.text((x,y),(" " * len(msg)), font=font, fill="white")
    virtual.set_position((0, 0))

def shutdown_handler(_signo, _stack_frame):
    global stopnow
    stopnow = 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')

    args = parser.parse_args()
    signal.signal(signal.SIGTERM, shutdown_handler)

    try:
        # create matrix device
        serial = spi(port=0, device=0, gpio=noop())
        device = max7219(serial, cascaded=args.cascaded, block_orientation=args.block_orientation, rotate=args.rotate or 0)
        virtual = viewport(device, width=fw*(maxwidth+1), height=1 * 8)
        device.contrast(0)
        clock()
    except KeyboardInterrupt:
        pass
