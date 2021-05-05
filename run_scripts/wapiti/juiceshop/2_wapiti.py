#!/usr/bin/python3

import subprocess
import os
import time

#get rename
subprocess.call("sudo apt install rename", shell=True)

#move dir
os.chdir("../../../")

#auth string
login = "admin@juice-sh.op"+"%"+"admin123"

#form the command
cmd = "wapiti -u http://localhost:3000 --scope domain -d 10 -a %s --auth-type=post -s http://localhost:3000/#/login --flush-session  -m all -l 2 -S aggressive -o ./reports/wapiti/juiceshop" %login

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
os.chdir("./reports/wapiti/juiceshop")
subprocess.call("rename 's/localhost_3000_.*.html/wapiti_juiceshop_report.html/' *", shell=True)

#persist the window to view results
#input("\n Press enter to close window...")