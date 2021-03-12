# fuzzingNode.jsApplications
## By BSH Tech

### This is a project aimed at fuzzing Node.js applications and reporting on their ability to detect security vulnerabilities.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Project Notes ##

*Requirements:*

-Python/pip

-Node

### *Setup:*

You may need to set the below environment variables for ZAP before running (location will depend on system - ubuntu is found in "/etc/environment.txt" - requires restart!). Since moving to a local version of zap I have not checked to see if this still needs to be done, so if you get errors when running zap do this bit.

`ZAP_PORT=8080`

`ZAP_PATH="<path_to_zap.sh>"`

`ZAP_URL="http://localhost"`

`ZAP_API_KEY="<your_zap_api_key>"`

To find your api key: Open ZAP -> Tools -> Options -> API

More info on api keys here: https://www.zaproxy.org/faq/why-is-an-api-key-required-by-default/

### *Fuzzing:*

For each fuzzer/application combination there is a specific folder with a master "run.py" script as well as helper scripts to launch all setup/fuzzing/reporting for that specific combination. These are all found in the "run_scripts" folder.

To mark each script as executable:

`chmod +x "<script_name.py>"`

Once all are executable, launch master script via: 

`./run.py`

This will launch that specific fuzzer against that specifc application.

### *Misc. Notes:*

In each script, file paths have been written to be local to this project so they shouldn't need changing, however if this changes in future revisions, all file directory commands can be found starting with: `os.chdir(<file_path>)`

Where possible, each `run.py` will produce a report of findings - these are stored in the 'reports' folder and will follow the format "fuzzer_application_report.html"

