#!/usr/bin/python3

import subprocess
import os

subprocess.call("sudo apt install rename", shell=True)

os.chdir("../../../")

#form the command
cmd = "wapiti -u http://localhost:3000 --flush-session --scope domain -o ./reports/wapiti"

#crawl & scan & save report - native+sqlmap+wapiti
subprocess.call(cmd, shell=True)

#re-name report
os.chdir("./reports/wapiti")
subprocess.call("rename 's/localhost_3000_.*.html/wapiti_juiceshop_report.html/' *", shell=True)

#persist the window to view results
#input("\n Press enter to close window...")