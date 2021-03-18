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
print("\n")
start = time.time()

#run authenticated scan on juiceshop through zap
#subprocess.call('zap-cli -v quick-scan --spider -r -c zap-juiceshop-context -u admin http://localhost:3000', shell=True)
subprocess.call('zap-cli -v quick-scan --ajax-spider -r -c zap-juiceshop-context -u admin http://localhost:3000', shell=True)

#change directory to where report should be saved
os.chdir("./../reports")

#export results as html file
subprocess.call('zap-cli report -o zap_juiceshop_report.html -f html', shell=True)

#print run time
end = time.time()
print("\nRUN TIME (minutes):")
print((int)(end-start)/60)

#persist the window to view output
# input("\n Press enter to close window...")

#depreciated/old stuff - to delete at a later date
#subprocess.call('zap-cli quick-scan --spider http://localhost:3000', shell=True)
#subprocess.call('zap-cli quick-scan --ajax-spider http://localhost:3000', shell=True)