# fuzzingNode.jsApplications
## By BSH Tech

### This is a project aimed at fuzzing Node.js applications and reporting on their ability to detect security vulnerabilities.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Temporary setup notes ##

Requirements:

-Python/pip

-Node

You may need to set the below environment variables for ZAP before running (location will depend on system - ubuntu is found in "/etc/environment.txt" - requires restart!). Since moving to a local version of zap I have not checked to see if this still needs to be done, so if you get errors when running zap do this bit.

`ZAP_PORT=8080`

`ZAP_PATH="<path_to_zap.sh>"`

`ZAP_URL="http://localhost"`

`ZAP_API_KEY="<your zap api key>"`

More info on api key here: https://www.zaproxy.org/faq/why-is-an-api-key-required-by-default/

For each fuzzer/application combination there is specific folder with a run.py script to launch all setup/fuzzing/reporting for that specific combination. These are all found in the "run_scripts" folder.

To mark each script as executable:

`chmod +x "script_name.py"`

Once all are executable, launch master script via: 

`./run.py`

This will launch that specific fuzzer against that specifc application.

In each script, file paths have been written to be local to this project so they shouldn't need changing, however if this changes in future revisions all file directory commands are called using `os.chdir(...file_path...)`

