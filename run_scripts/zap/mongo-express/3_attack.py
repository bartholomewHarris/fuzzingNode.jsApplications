#!/usr/bin/python3

import subprocess
import os
import time
import sys

#move directories to zap install location
os.chdir("./../../../ZAP_2.10.0")

#import configured context
subprocess.call('zap-cli context import admin-express.context', shell=True)

#disable auth script if present
subprocess.call('zap-cli scripts disable auth.js', shell=True)

#start timer
start1 = time.time()

#crawl
subprocess.call('zap-cli open-url http://localhost:8081', shell=True)
subprocess.call('zap-cli -v spider -c admin-express -u admin http://localhost:8081', shell=True)
subprocess.call('zap-cli -v ajax-spider admin:pass@localhost:8081', shell=True)

#calculate scan time
end1 = time.time()
total1 = round(((end1-start1)/60), 2)

#start timer
start2 = time.time()

#scan
subprocess.call('zap-cli -v active-scan -r -c admin-express -u admin http://localhost:8081', shell=True)

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
subprocess.call('zap-cli report -o zap_mongoexpress_report.html -f html', shell=True)

#persist the window to view output
# input("\n Press enter to close window...")