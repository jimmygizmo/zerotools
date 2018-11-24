#! /usr/bin/env python3

import psutils
import time

SCAN_INTERVAL = 5000  # Milliseconds between scans of the process table.
# Be careful with SCAN_INTERVALS below 2000 milliseconds as scanning
# the process table can put demands on system resources and even in the best
# of circumstances can take multiple seconds to complete.
# In any case, the actual frequency of scans can be no faster than the current
# conditions allow for the completion of a scan.


##
#
