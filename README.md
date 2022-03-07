# BBSOTimetable
Telegram bot in Python for getting current timetable of BBSO-01-21 group.

## Requirements
`python >= 3.10`

`pyTelegramBotAPI == 4.4.0`

## Run
1. `pip install -r requirements.txt`
2. `python src/main.py`

## Environment variables
1. `BOT_TOKEN` - token bot
2. `HOOK_SERVER` - ip or domain of server where bot is serving, if ignored polling is used
3. `HOOK_URL` - url of hook, if ignored random url is used
4. `HOOK_PORT` - port `default:8080`


## Docker
### Running container example
If you want to use webhook
1. `docker run -d --name bot -eBOT_TOKEN='YOUR_TOKEN' -eHOOK_SERVER='YOUR_URL_OR_IP' -eHOOK_PORT=443 -p 0.0.0.0:443:443 bbso_bot`

If you want polling
1. `docker run -d --name bot -eBOT_TOKEN='YOUR_TOKEN' bbso_bot`

### Creating docker image from source
1. `make docker`

### Running docker image(polling)
1. `export BOT_TOKEN='YOUR_TOKEN'`
2. `make docker-run`

### Saving docker image to tar.gz
1. `make docker-save`

### Deleting image for docker local repository
1. `make docker-clean`

## Generating certificates
1. `openssl req -newkey rsa:2048 -sha256 -nodes -keyout private.key -x509 -days 365 -out public.pem` in src directory
2. `make`

Your docker image with your keys is ready
