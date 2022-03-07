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


## Docker
### Creating docker image from source
1. `make docker`

### Running docker image
1. `export BOT_TOKEN='YOUR_TOKEN'`
2. `make docker-run`

### Saving docker image to tar.gz
1. `make docker-save`

### Deleting image for docker local repository
1. `make docker-clean`
