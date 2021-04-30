#!/usr/bin/python3

import time
import os

#launch juiceshop
os.system("gnome-terminal -- python3 1_mongo-express.py")

#wait for juiceshop to startup
time.sleep(7)

#launch htcap attack
os.system("gnome-terminal -- python3 2_htcap.py")