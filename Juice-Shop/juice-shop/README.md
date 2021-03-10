## Temporary setup notes ##

Requirements:

-OWASP Zap

-Python/pip (If using 3+, change 'raw_input' in 3_attack.py to 'input')

-Node

You will need to set the below environment variables (location will depend on system - ubuntu is found in "/etc/environment.txt" - requires restart!)

`ZAP_PORT=8080`

`ZAP_PATH="<path_to_zap.sh>"`

`ZAP_URL="http://localhost"`

`ZAP_API_KEY="<your zap api key>"`


To mark each script as executable:

`chmod +x run.py`

`chmod +x 1_juiceshop.py`

`chmod +x 2_zap.py`

`chmod +x 3_attack.py`

Once all are executable, launch master script via: 

`./run.py`

This will launch juice shop, ZAP in Daemon mode and after a short setup period will run a basic spider + scan, then save the results to an html file.

*NOTE:* There are file paths specified in the scripts that will need to be altered to reflect your own file path/s - these are denoted anywhere starting os.chdir(....) - So you'll need to determine where "zap.sh" is located on your machine and replace the locations with that, as well as setting where you want the report to be saved to.

### From Sources

![GitHub repo size](https://img.shields.io/github/repo-size/bkimminich/juice-shop.svg)

1. Install [node.js](#nodejs-version-compatibility)
3. Go into the cloned folder with `cd juice-shop`
4. Run `npm install` (only has to be done before first start or when you change the source code)
5. Run `npm start`
6. Browse to <http://localhost:3000>

## FOR REFERENCE ONLY ##
### Docker Container

[![Docker Pulls](https://img.shields.io/docker/pulls/bkimminich/juice-shop.svg)](https://hub.docker.com/r/bkimminich/juice-shop)
![Docker Stars](https://img.shields.io/docker/stars/bkimminich/juice-shop.svg)
[![](https://images.microbadger.com/badges/image/bkimminich/juice-shop.svg)](https://microbadger.com/images/bkimminich/juice-shop
"Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/bkimminich/juice-shop.svg)](https://microbadger.com/images/bkimminich/juice-shop
"Get your own version badge on microbadger.com")

1. Install [Docker](https://www.docker.com)
2. Run `docker pull bkimminich/juice-shop`
3. Run `docker run --rm -p 3000:3000 bkimminich/juice-shop`
4. Browse to <http://localhost:3000> (on macOS and Windows browse to
   <http://192.168.99.100:3000> if you are using docker-machine instead

