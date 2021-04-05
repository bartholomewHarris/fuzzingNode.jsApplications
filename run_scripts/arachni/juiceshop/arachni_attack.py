#!/usr/bin/python

import subprocess
import os

os.chdir("./../../../arachni-1.5.1-0.5.12/bin")

subprocess.call('./arachni --output-verbose --output-only-positives --scope-include-subdomains --scope-exclude-pattern http://127.0.0.1:3000/redirect \
    --report-save-path /reports/arachni_juiceshop_report http://127.0.0.1:3000', shell=True)