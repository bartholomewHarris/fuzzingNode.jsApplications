#!/usr/bin/python3

import subprocess
import os

#get rename
subprocess.call("sudo apt install rename", shell=True)

#move dir
os.chdir("../../../")

#auth string
login = "admin@juice-sh.op"+"%"+"admin123"

#form the command
cmd = "wapiti -u http://localhost:3000 --scope domain -d 10 -a %s --auth-type=post -s http://localhost:3000/#/login --flush-session  -m all -l 2 -S aggressive -o ./reports/wapiti" %login

#crawl & scan & save report - native+sqlmap+wapiti
subprocess.call(cmd, shell=True)

#re-name and save report
os.chdir("./reports/wapiti")
subprocess.call("rename 's/localhost_3000_.*.html/wapiti_juiceshop_report.html/' *", shell=True)

#persist the window to view results
#input("\n Press enter to close window...")