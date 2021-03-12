#!/usr/bin/python

import os
import time

#launch juiceshop
os.system("gnome-terminal -- python 1_juiceshop.py")

#launch zap in daemon mode
os.system("gnome-terminal -- python 2_zap.py")

#wait for the above to boot
time.sleep(20)

#launch attack script
os.system("gnome-terminal -- python 3_attack.py")
