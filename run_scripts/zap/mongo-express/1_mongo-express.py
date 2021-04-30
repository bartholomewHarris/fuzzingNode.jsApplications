#!/usr/bin/python

import subprocess
import os

# start mongodb
subprocess.call('sudo systemctl start mongod', shell=True)

# start mongo-express
subprocess.call('mongo-express -H localhost -P 27017', shell=True)

#start up juice shop application on port 3000
subprocess.call('npm start', shell=True)