#!/usr/bin/python3

import subprocess
import os
import time

#get rename
subprocess.call("sudo apt install rename", shell=True)

#move dir
os.chdir("../../../")

#auth string
login = "admin"+"%"+"Admin_123"

#form the command
cmd = "wapiti -u http://localhost:4000 --scope domain -d 10 -a %s --auth-type=post -s http://localhost:4000/login --flush-session -l 2 -S normal --color -m all --max-attack-time 10800 -o ./reports/wapiti/nodegoat" %login

#start timer
start1 = time.time()

#crawl & scan & save report
subprocess.call(cmd, shell=True)

#calculate run time
end1 = time.time()
total1 = round(((end1-start1)/60), 2)

#print run times
print("\nTOTAL TIME (minutes):")
print((int)(total1))

#re-name and save report
os.chdir("./reports/wapiti/nodegoat")
subprocess.call("rename 's/localhost_4000_.*.html/wapiti_nodegoat_report.html/' *", shell=True)

#persist the window to view results
# input("\n Press enter to close window...")