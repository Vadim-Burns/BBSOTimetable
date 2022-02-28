import telebot
from keyboards import main_markup
from config import BOT_TOKEN
from timetable import get_today_timetable, get_tomorrow_timetable, get_after_tomorrow_timetable, \
    get_current_week_timetable, get_next_week_timetable

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здарова, путник", reply_markup=main_markup)


@bot.message_handler(content_types=['text'])
def process_keyboard(message):
    if message.text == "Расписание на сегодня":
        bot.send_message(message.chat.id, get_today_timetable())
    elif message.text == "Расписание на завтра":
        bot.send_message(message.chat.id, get_tomorrow_timetable())
    elif message.text == "Расписание на послезавтра":
        bot.send_message(message.chat.id, get_after_tomorrow_timetable())
    elif message.text == "Расписание на текущую неделю":
        for day in get_current_week_timetable():
            bot.send_message(message.chat.id, day)
    elif message.text == "Расписание на следующую неделю":
        for day in get_next_week_timetable():
            bot.send_message(message.chat.id, day)


if __name__ == '__main__':
    print("Bot has been started!")
    bot.infinity_polling()
