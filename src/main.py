import telebot
from keyboards import main_markup
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello there?", reply_markup=main_markup)


if __name__ == '__main__':
    bot.infinity_polling()
