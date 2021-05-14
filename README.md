# fuzzingNode.jsApplications
## By BSH Tech

### This is a project aimed at fuzzing Node.js applications and reporting on their ability to detect security vulnerabilities.

---------------------------------------------------

Fuzzers Used:

- [OWASP Zap](https://www.zaproxy.org/)

- [htcap](https://htcap.org/)

- [W3af](https://w3af.org/)

- [Wapiti](https://wapiti.sourceforge.io/)

- [Arachni](https://www.arachni-scanner.com/)

----------------------------------------------------

Applications Analysed:

- [JuiceShop](https://github.com/bkimminich/juice-shop)

- [Nodegoat](https://github.com/OWASP/NodeGoat)

- [Mongo Express](https://github.com/mongo-express/mongo-express)

----------------------------------------------------

## Project Notes ##

### *Steps to run:*

In the top menu in GitHub, click through to *Actions*. From here select which combination you would like to launch, click *Run workflow*, then the green *Run workflow* button in the drop down. Actions can be a little laggy so it may take approx 5-20 seconds for it to show up after launch. Once running you can watch the job logging, or just come back for the report once done. 

Each combination varies widely in how long it can take to run, so some can be done in a few minutes while others will take up to (the maximum allowed) 6 hours. 

Reports are not kept in the `reports` folder - this is really just for local testing/running, but will be available to download once the job has completed by clicking through to it under the *Artifacts* section.

----------------------------------------------------

### *Running Locally:*

*NOTE: This will require some setup that is not detailed here, specifically:*

*- Install and set up [mongobd](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)*

*- Install and set up [mongo-express](https://github.com/mongo-express/mongo-express)*

*- Install [Python/pip](https://www.python.org/downloads/source/)*

*- Install [node/npm](https://www.geeksforgeeks.org/installation-of-node-js-on-linux/)*

*- Install [wapiti](https://wapiti.sourceforge.io/)*

*- Install [zap-cli](https://github.com/Grunny/zap-cli)*

*- Set Zap Environment variables - instructions below*

*- Place config.js into `PATH/node_modules/mongo-express/`*

*- Init/use an empty db called `exampledb` in mongodb and run `4_mongodb_init.py` from any run_scripts mongo folder*

*- Ensure ports 3000, 4000, 8081 and 27017 are not currently in use*

----------------------------------------------------

If you would prefer to run fuzzers locally, simply clone the repo and navigate to the `run_scripts` folder

For each fuzzer/application combination there is a specific folder with a master "run.py" script as well as helper scripts to launch all setup/fuzzing/reporting for that specific combination.

To launch a fuzzer against an application, open a terminal in the target folder and enter:

`./run.py`

This will launch the required scripts to set up, crawl, scan and save the resultant output in the `reports` folder. If you encounter errors use the logs/output to determine what the issue is. It's possible some dependencies are required but have not been identified above.

*NOTE: All scripts have been written in Python and assume the user is running a (relatively) modern version of Ubuntu. Other distributions have not been tested, however assuming you have gnome terminal installed (along with the other requirements outlined above) it should work - You could also just replace gnome-terminal in each run.py with the terminal of your choice*

----------------------------------------------------

### *Zap Environment variables:*

You will need to set the below environment variables for ZAP before running locally (location will depend on system - ubuntu is found in "/etc/environment.txt" - requires restart!)

`ZAP_PORT=8080`

`ZAP_PATH="<path_to_zap.sh>"`

`ZAP_URL="http://localhost"`

`ZAP_API_KEY="<your_zap_api_key>"`

To find your api key: Open ZAP -> Tools -> Options -> API

More info on api keys here: https://www.zaproxy.org/faq/why-is-an-api-key-required-by-default/

----------------------------------------------------

### *Misc. Notes:*

In each script, file paths have been written to be local to this project so they shouldn't need changing, however if this changes in future revisions, all file directory commands can be found starting with: `os.chdir(<file_path>)`

When run locally, each `run.py` will produce a report of findings - these are stored in the 'reports' folder and will follow the format "<fuzzer>_<application>_report.html"
  
You can uncomment the final line of each 'attack' script to show the run times of each process
