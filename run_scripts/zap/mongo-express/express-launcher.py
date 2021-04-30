#!/usr/bin/python

import subprocess

subprocess.call('mongo-express -H localhost -P 27017', shell=True)
