#! /usr/bin/env python3

# https://pymotw.com/3/threading/

# To see thread details (system call trace), the PID of the process of the
# filament program must be known and this can be obtained using something like:
# ps aux | grep filament
# This must be done BEFORE the threads are created, hence the time.sleep near
# the beginning of this prgram must be used to allow time for this grep.
# Then as sudo, the dtruss utility will be used to monitor the threads from
# the TIME OF THREAD CREATION for the now-known PID of filament.py, with this
# command:
# sudo dtruss -ap PID
# This must be done as root hence the sudo. Substite the grepped PID.
# If the threads have already been created when the dtruss command is run then
# no output will be seen.
#

import curses
import threading
import uuid
import random
import time

DEVMODE = True
NUMTHREADS = 2

scrn = curses.initscr()
curses.noecho()  # Don't echo keypresses to terminal
curses.cbreak()  # Realtime keypress response (no enter-key buffering)
scrn.keypad(True)  # Enable label access to special keys (e.g. curses.KEY_LEFT)

# Curses coordinate system is (Y, X) with (0, 0) top-left
# Y range of lines is 0 to LINES - 1. X range of columns is 0 to COLS - 1.
mainheight = curses.LINES
mainwidth = curses.COLS
mainmax_y = mainheight - 1
mainmax_x = mainwidth - 1

if DEVMODE:
    print ("Screen height: {} - Screen width: {}"
           .format(mainheight, mainwidth))

MUCHMETAL = "platinum gold silver copper iron aluminum zinc lead nickel "\
            "cobalt chromium titanium tungsten magnesium mercury lithium "\
            "sodium uranium manganese aluminum potassium cobalt"
CHOICES = 8

metals = MUCHMETAL.split()

# Use this sleep here before thread creation to be able to grep the PID
# of filament.py to use in the dtruss command when you want to see thread
# details. 30 seconds should be enough time to grep and then run dtruss.
time.sleep(30)


def get_uuid():
    return uuid.uuid4()


#  THREAD - BASIC
#  ############################################################################
def worker(seqid, uniqueid):
    threadname = threading.current_thread().getName()
    randlist = []
    for r in range(CHOICES):
        randlist.append(random.choice(metals))

    if DEVMODE:
        print ("---------------------------------------------------------")
        print ("Sequence ID: {} - UUID: {}".format(seqid, uniqueid))
        print ("Threadname: {}".format(threadname))
        print ("Random metals: {}".format("-".join(randlist)))
#  ############################################################################


threads = []


def launch_threads_basic():
    for seqid in range(NUMTHREADS):
        uniqueid = get_uuid()
        t = threading.Thread(target=worker, args=(seqid, uniqueid))
        threads.append(t)
        t.start()


launch_threads_basic()

time.sleep(10)

#  Return terminal window to normal behavior and release it from curses
curses.nocbreak()
scrn.keypad(False)
curses.echo()
curses.endwin()

##
#
