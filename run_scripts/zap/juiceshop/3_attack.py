#!/usr/bin/python3

import subprocess
import os
import time
import sys

#move directories to zap install location
os.chdir("./../../../ZAP_2.10.0")

#import configured context
subprocess.call('zap-cli context import ./zap-juiceshop-context.context', shell=True)

#load auth script - debug on
subprocess.call('zap-cli -v scripts load -n auth.js -t "httpsender" -e "Oracle Nashorn" -f ./scripts/auth.js', shell=True)

#enable auth script
subprocess.call('zap-cli scripts enable auth.js', shell=True)

#start timer
start1 = time.time()

#crawl
subprocess.call('zap-cli open-url http://localhost:3000', shell=True)
subprocess.call('zap-cli -v spider -c zap-juiceshop-context -u admin http://localhost:3000', shell=True)
subprocess.call('zap-cli -v ajax-spider http://localhost:3000', shell=True)

#calculate scan time
end1 = time.time()
total1 = round(((end1-start1)/60), 2)

#start timer
start2 = time.time()

#scan
subprocess.call('zap-cli -v active-scan -r -c zap-juiceshop-context -u admin http://localhost:3000', shell=True)

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
subprocess.call('zap-cli report -o zap_juiceshop_report.html -f html', shell=True)

#persist the window to view output
# input("\n Press enter to close window...")