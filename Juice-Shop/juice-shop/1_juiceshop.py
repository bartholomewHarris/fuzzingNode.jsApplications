#!/usr/bin/python

import subprocess

#install zap-cli used for making zap api calls
subprocess.call('pip install --upgrade zapcli', shell=True)

#start up juice shop application on port 3000
subprocess.call('npm start', shell=True)

