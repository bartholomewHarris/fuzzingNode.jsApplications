#!/usr/bin/python3

import subprocess
import os
import time

#change to htcap directory
os.chdir('./../../../htcap')
os.chdir('core/nodejs')
subprocess.call("npm i", shell=True)
os.chdir('../../')

#easy way to change spider run time in seconds - e.g. (3 hours = 10800)
SPIDERTIME = 10800

#start timer
start1 = time.time()

#form the command
crawl = "./htcap.py crawl -w -t %d -x http://localhost:3000/redirect. -L login.json localhost:3000 htcap_juiceshop_report.db" % SPIDERTIME

#crawl - native+sqlmap+wapiti
subprocess.call(crawl, shell=True)

#calculate crawl time
end1 = time.time()
total1 = round(((end1-start1)/60), 2)

#start timer
start2 = time.time()

#scan with native, wapiti and sqlmap
scan = "./htcap.py scan native htcap_juiceshop_report.db \; scan wapiti htcap_juiceshop_report.db \; scan sqlmap htcap_juiceshop_report.db"
subprocess.call(scan, shell=True)

#end timer
end2 = time.time()
total2 = round(((end2-start2)/60), 2)

#gen report
report = "./htcap.py util report htcap_juiceshop_report.db htcap_juiceshop_report.html"
subprocess.call(report, shell=True)

#move the report to the report folder
subprocess.call('mv htcap_juiceshop_report.html ./../reports', shell=True)

#print run times
print("\nCRAWL TIME (minutes):")
print((int)(total1))
print("\nSCAN TIME (minutes):")
print((int)(total2))

#persist the window to view results
# input("\n Press enter to close window...")