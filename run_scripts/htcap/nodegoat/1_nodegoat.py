#!/usr/bin/python3

import subprocess
import os

#change directories to nodegoat
os.chdir('./../../../nodegoat/NodeGoat')

#init mongodb
subprocess.call('sudo systemctl start mongod', shell=True)
subprocess.call('npm run db:seed', shell=True)

#start up node goat on port 4000
subprocess.call('npm start', shell=True)