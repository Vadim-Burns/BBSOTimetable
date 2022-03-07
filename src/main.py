from bot import bot
from flask import Flask, request
from config import HOOK_URL, HOOK_SERVER, HOOK_PORT
import telebot

app = Flask(__name__)


@app.route(f"/{HOOK_URL}", methods=['POST'])
def hook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


if __name__ == '__main__':
    bot.remove_webhook()

    if HOOK_SERVER != "":
        bot.set_webhook(url=f"https://{HOOK_SERVER}:{HOOK_PORT}/{HOOK_URL}")
        print(f"Webhook set on https://{HOOK_SERVER}:{HOOK_PORT}/{HOOK_URL}", flush=True)

        print("Starting flask", flush=True)
        app.run(host='0.0.0.0', port=HOOK_PORT)

    else:
        print("Bot has been started!", flush=True)
        bot.infinity_polling()
