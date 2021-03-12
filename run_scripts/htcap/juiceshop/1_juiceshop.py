#!/usr/bin/python3

import subprocess
import os

#install zap-cli used for making zap api calls
subprocess.call('pip install --upgrade zapcli', shell=True)

#change directories to juiceshop
os.chdir('./../../../Juice-Shop/juice-shop')

#start up juice shop application on port 3000
subprocess.call('npm start', shell=True)