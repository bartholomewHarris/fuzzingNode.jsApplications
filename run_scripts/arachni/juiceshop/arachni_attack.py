#!/usr/bin/python

import subprocess
import os

os.chdir("./../../../arachni-1.5.1-0.5.12/bin")

hostname = subprocess.check_output(["hostname"])
hostname = hostname.decode("utf-8")

target = "http://" + hostname 
target = target.rstrip("\n")
target = target + ":3000"

exclude = target + "/redirect"

command = "./arachni --output-verbose --output-only-positives --scope-include-subdomains --scope-exclude-pattern "
command = command + exclude + " --report-save-path arachni_juiceshop_report.afr --timeout 0:3:0 "
command = command + "--http-authentication-username admin@juice-sh.op --http-authentication-password admin123 " + target

subprocess.call(command, shell=True)