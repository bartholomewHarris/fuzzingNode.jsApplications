#!/usr/bin/python

import os
import time

#launch zap in daemon mode
os.system("gnome-terminal -- python 2_zap.py")

#launch juiceshop
os.system("gnome-terminal -- python 1_mongo-express.py")

#wait for the above to boot
time.sleep(10)

#launch attack script
os.system("gnome-terminal -- python 3_attack.py")
