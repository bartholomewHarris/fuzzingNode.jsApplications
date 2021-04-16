#!/usr/bin/python3

import subprocess
import os

#change to htcap directory
os.chdir('./../../../htcap')

#easy way to change spider run time in seconds - e.g. (3 hours = 10800)
SPIDERTIME = 20

#form the command
cmd = "htcap crawl -w -t %d -x http://localhost:3000/redirect. http://localhost:3000/ htcap_juiceshop_report.db \; scan native \; scan wapiti \; scan sqlmap \; util report htcap_juiceshop_report.html" % SPIDERTIME

#crawl & scan & save report - native+sqlmap+wapiti
subprocess.call(cmd, shell=True)

#move the report to the report folder
subprocess.call('mv htcap_juiceshop_report.html ./../reports', shell=True)

#persist the window to view results
#input("\n Press enter to close window...")