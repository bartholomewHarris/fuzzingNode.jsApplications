#!/usr/bin/python

import subprocess
import os

os.chdir("./../../../arachni-1.5.1-0.5.12/bin")

hostname = subprocess.check_output(["hostname"])

target = "http://" + hostname + ":3000"

exclude = target + "/redirect"

command = "'./arachni --output-verbose --output-only-positives --scope-include-subdomains --scope-exclude-pattern "
command = command + exclude + " --report-save-path /reports/arachni_juiceshop_report " + target + "'"

subprocess.call(command, shell=True)