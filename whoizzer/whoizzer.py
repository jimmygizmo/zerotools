#! /usr/bin/env python3

import sys
import subprocess

#COMMAND_WITH_OPTIONS = '/usr/bin/whois'
COMMAND_WITH_OPTIONS = 'whois'

arg = sys.argv[1]

if '.' not in arg:
    arg = f"{arg}.com"

cmd = f"{COMMAND_WITH_OPTIONS} {arg}"

res = subprocess.check_output(cmd, stderr=None, shell=True)

res_string = res.decode("utf-8")  # Weird but a bytearray is returned
res_arr = res_string.split("\n")  # Makes a list of the lines

print()
for line in res_arr:
    if r'Domain Name: ' in line:
        print(line)
    if r'Registrar: ' in line:
        print(line)
    if r'Creation Date: ' in line:
        print(line)
    if r'No match for domain' in line:
        #print(line)
        print('* * * * AVAILABLE * * * *')

print()

##
#

