#!/usr/bin/python3

import subprocess
import os

#change to htcap directory
os.chdir('./../../../htcap')

#crawl & scan & save report- native/default
subprocess.call('./htcap.py crawl -w -t 60 -x http://localhost:3000/redirect. http://localhost:3000 htcap_juiceshop_report.db \; scan native \; scan arachni \; scan sqlmap \; util report htcap_juiceshop_report.html', shell=True)

#move the report to the report folder
subprocess.call('mv htcap_juiceshop_report.html ./../reports', shell=True)

#persist the window to view results
input("\n Press enter to close window...")