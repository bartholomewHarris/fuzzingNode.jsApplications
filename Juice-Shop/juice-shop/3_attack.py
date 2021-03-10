#!/usr/bin/python

import subprocess
import os

#move directories to zap install location - THIS IS SPECIFIC TO MY SYSTEM
os.chdir("/snap/zaproxy/5")

#run basic scan on juiceshop through zap
subprocess.call('zap-cli quick-scan --spider http://localhost:3000', shell=True)

#change directory to where report should be saved
os.chdir("/home/william/Documents")

#export results as html file
subprocess.call('zap-cli report -o zap_report_juiceshop.html -f html', shell=True)

#persist the window to view results
raw_input("\n Press enter to close window...")