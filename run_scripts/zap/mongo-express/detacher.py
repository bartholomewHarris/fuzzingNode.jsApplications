#!/usr/bin/python

import os
import subprocess

subprocess.call('sudo apt update', shell=True)
subprocess.call('sudo apt install gnome-terminal', shell=True)

os.system("gnome-terminal -- python express-launcher.py")
