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
# If the threads have already been creaed when the dtruss command is run then
# no output will be seen.
#

import threading
import uuid
import random
import time

NUMTHREADS = 2
DEVMODE = True
MUCHMETAL = "platinum gold silver copper iron aluminum zinc lead nickel "\
            "cobalt chromium titanium tungsten magnesium mercury lithium "\
            "sodium"
CHOICES = 8

metals = MUCHMETAL.split()

# Use this sleep here before thread creation to be able to grep the PID
# of filament.py to use in the dtruss command when you want to see thread
# details. 30 seconds should be enough time to grep and then run dtruss.
time.sleep(30)


def get_uuid():
    return uuid.uuid4()


#  BASIC THREAD
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

##
#
