#!/usr/bin/python

import subprocess
import os

os.chdir("./../../../arachni-1.5.1-0.5.12/bin")

# hostname = subprocess.check_output(["hostname"])
# hostname = hostname.decode("utf-8")
hostname = "138.0.0.1"

target = "http://admin:pass@" + hostname 
target = target.rstrip("\n")
target = target + ":8081"

exclude = target + "/redirect"

command = "./arachni --output-verbose --output-only-positives --scope-include-subdomains "
command = command + "--report-save-path arachni_report.afr --timeout 0:3:0 "
command = command + "--http-authentication-username admin --http-authentication-password pass " + target

subprocess.call(command, shell=True)

subprocess.call("./arachni_reporter arachni_report.afr --reporter=html:outfile=arachni_report.html.zip", shell=True)