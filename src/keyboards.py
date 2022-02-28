from telebot import types

main_markup = types.ReplyKeyboardMarkup()
current_day = types.KeyboardButton('Расписание на сегодня')
tomorrow_day = types.KeyboardButton('Расписание на завтра')
after_tomorrow_day = types.KeyboardButton('Расписание на послезавтра')
week = types.KeyboardButton('Расписание на текущую неделю')
next_week = types.KeyboardButton('Расписание на следующую неделю')
main_markup.row(current_day)
main_markup.row(tomorrow_day)
main_markup.row(after_tomorrow_day)
main_markup.row(week)
main_markup.row(next_week)
