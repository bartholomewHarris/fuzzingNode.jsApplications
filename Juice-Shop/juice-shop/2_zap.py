#!/usr/bin/python

import subprocess
import os

#move directories to zap install location - THIS IS SPECIFIC TO MY SYSTEM
os.chdir("/snap/zaproxy/5")

#launch zap in daemon mode
subprocess.call('./zap.sh -daemon', shell=True)

