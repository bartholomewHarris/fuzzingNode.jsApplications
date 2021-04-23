#!/usr/bin/python3

import time
import os

#launch juiceshop
os.system("gnome-terminal -- python 1_nodegoat.py")

#wait for juiceshop to startup
time.sleep(12)

#launch htcap attack
os.system("gnome-terminal -- python 2_wapiti.py")