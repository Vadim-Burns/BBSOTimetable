.DEFAULT_GOAL := docker

docker:
	docker build -t bbso_bot .

docker-run:
	docker run --rm -eBOT_TOKEN=${BOT_TOKEN} bbso_bot

docker-save:
	docker save bbso_bot | gzip > bbso_bot.tar.gz

docker-clean:
	-docker image rm bbso_bot
	-rm bbso_bot.tar.gz