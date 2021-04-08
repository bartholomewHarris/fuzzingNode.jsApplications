#!/usr/bin/python3

import subprocess
import os

#form the command
cmd = "wapiti -u http://localhost:3000"

#crawl & scan & save report - native+sqlmap+wapiti
subprocess.call(cmd, shell=True)

#move the report to the report folder

#persist the window to view results
#input("\n Press enter to close window...")