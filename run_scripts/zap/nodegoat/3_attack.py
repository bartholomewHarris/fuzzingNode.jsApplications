#!/usr/bin/python3

import subprocess
import os
import time
import sys

#move directories to zap install location
os.chdir("./../../../ZAP_2.10.0")

#import configured context
subprocess.call('zap-cli context import NodeGoat-Auth.context', shell=True)

#disable auth script if present
subprocess.call('zap-cli scripts disable auth.js', shell=True)

#load auth script
# subprocess.call('zap-cli -v scripts load -n nodegoat-login.zst -t "Authentication" -e "Mozilla Zest" -f ./scripts/nodegoat-login.zst', shell=True)

#start timer
start1 = time.time()

#crawl
subprocess.call('zap-cli open-url http://localhost:4000', shell=True)
subprocess.call('zap-cli -v spider -c NodeGoat-Auth -u admin http://localhost:4000', shell=True)
subprocess.call('zap-cli -v ajax-spider http://localhost:4000', shell=True)

#calculate scan time
end1 = time.time()
total1 = round(((end1-start1)/60), 2)

#start timer
start2 = time.time()

#scan
subprocess.call('zap-cli -v active-scan -r -c NodeGoat-Auth -u admin http://localhost:4000', shell=True)

#calculate scan time
end2 = time.time()
total2 = round(((end2-start2)/60), 2)

#print run times
print("\nCRAWL TIME (minutes):")
print((int)(total1))
print("\nSCAN TIME (minutes):")
print((int)(total2))

#change directory to where report should be saved
os.chdir("./../reports")

#export results as html file
subprocess.call('zap-cli report -o zap_nodegoat_report.html -f html', shell=True)

#persist the window to view output
# input("\n Press enter to close window...")