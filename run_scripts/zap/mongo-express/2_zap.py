#!/usr/bin/python

import subprocess
import os

#move directories to zap install location
os.chdir("./../../../ZAP_2.10.0/")

#launch zap in daemon mode
subprocess.call('./zap.sh -daemon -config ajaxSpider.maxDuration=5', shell=True)

