#!/usr/bin/python3

import subprocess
import os

#get rename
subprocess.call("sudo apt install rename", shell=True)

#move dir
os.chdir("../../../")

#auth string
login = "admin"+"%"+"Admin_123"

#form the command
cmd = "wapiti -u http://localhost:4000 --scope domain -d 10 -a %s --auth-type=post -s http://localhost:4000/login --flush-session -l 2 -S normal --color -m all --max-attack-time 10800 -o ./reports/wapiti" %login

#crawl & scan & save report - native+sqlmap+wapiti
subprocess.call(cmd, shell=True)

#re-name and save report
os.chdir("./reports/wapiti")
subprocess.call("rename 's/localhost_4000_.*.html/wapiti_nodegoat_report.html/' *", shell=True)

#persist the window to view results
# input("\n Press enter to close window...")