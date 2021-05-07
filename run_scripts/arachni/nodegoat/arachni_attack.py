#!/usr/bin/python

import subprocess
import os

os.chdir("./../../../arachni-1.5.1-0.5.12/bin")

hostname = subprocess.check_output(["hostname"])
hostname = hostname.decode("utf-8")

target = "http://" + hostname 
target = target.rstrip("\n")
target = target + ":4000"

exclude = target + "/redirect"

command = "./arachni --output-verbose --output-only-positives --scope-include-subdomains --scope-exclude-pattern "
command = command + exclude + " --report-save-path arachni_report.afr --timeout 0:5:0 "
command = command + "--http-authentication-username admin --http-authentication-password Admin_123 " + target

subprocess.call(command, shell=True)

subprocess.call("./arachni_reporter arachni_report.afr --reporter=html:outfile=arachni_report.html.zip", shell=True)