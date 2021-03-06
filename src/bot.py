import logging

import telebot

from config import BOT_TOKEN
from keyboards import main_markup
from timetable import get_today_timetable, get_tomorrow_timetable, get_after_tomorrow_timetable, \
    get_current_week_timetable, get_next_week_timetable, get_current_week, get_current_group
from users_storage import update

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html")
telebot.logger.setLevel(logging.INFO)


@bot.message_handler(commands=['start'])
def start(message):
    update(message.from_user.username)
    bot.send_message(message.chat.id, "Здарова, путник", reply_markup=main_markup)


@bot.message_handler(commands=['week'])
def week(message):
    update(message.from_user.username)
    bot.send_message(message.chat.id, f"Текущая неделя под номером {get_current_week()}")


@bot.message_handler(commands=['group'])
def group(message):
    update(message.from_user.username)
    bot.send_message(message.chat.id, f"На этой неделе ходит группа {get_current_group(get_current_week())}")


@bot.message_handler(content_types=['text'])
def process_keyboard(message):
    update(message.from_user.username)
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
