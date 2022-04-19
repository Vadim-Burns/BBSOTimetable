import datetime

from config import START_WEEK, EVEN_WEEK, UNEVEN_WEEK, SPECIALS, LESSONS_TIME, WEEKDAY_NAMES


def get_current_week() -> int:
    cur_week = datetime.datetime.now().isocalendar().week
    return cur_week - START_WEEK + 1


def get_current_weekday() -> int:
    return datetime.datetime.now().isocalendar().weekday


def get_lessons(weekday: int, week: int) -> list:
    lessons = []

    if week % 2 == 0:
        for lesson in EVEN_WEEK.get(weekday):
            lessons.append(lesson)
    else:
        for lesson in UNEVEN_WEEK.get(weekday):
            lessons.append(lesson)

    for lesson in SPECIALS.get((weekday, week), []):
        lessons.append(lesson)

    lessons = sorted(lessons, key=lambda x: x[0])

    return lessons


def get_timetable(weekday: int, week: int) -> str:
    if weekday == 7:
        return "Воскресенье.\nОтдыхай, брат"
    elif weekday == 6 and week % 2 == 1:
        return "Вроде френч, но пока хз.\nОтдыхай, брат"
    elif weekday == 6:
        return "Вроде как практика, но хуй его знает.\nОтдыхай, брат"
    elif weekday == 5:
        return "Для тебя нихуя.\nОтдыхай, брат"

    lessons = get_lessons(weekday, week)
    msg = ""

    for lesson in lessons:
        msg += "<b>" + str(lesson[0]) + ". " + LESSONS_TIME[lesson[0]] + "</b>\n" + lesson[1] + "\n"

    return msg


def get_today_timetable() -> str:
    weekday = get_current_weekday()
    cur_week = get_current_week()

    return get_timetable(weekday, cur_week)


def get_tomorrow_timetable() -> str:
    weekday = get_current_weekday() + 1
    cur_week = get_current_week()

    if weekday > 7:
        cur_week += 1
        weekday = 1

    return get_timetable(weekday, cur_week)


def get_after_tomorrow_timetable() -> str:
    weekday = get_current_weekday() + 2
    cur_week = get_current_week()

    if weekday > 7:
        cur_week += 1
        weekday = weekday % 7

    return get_timetable(weekday, cur_week)


def get_current_week_timetable() -> list[str]:
    days = []
    cur_week = get_current_week()

    for weekday in range(1, 6):
        days.append(
            "<i>" + WEEKDAY_NAMES[weekday] + "</i>\n" + get_timetable(weekday, cur_week)
        )

    return days


def get_next_week_timetable() -> list[str]:
    days = []
    cur_week = get_current_week() + 1

    for weekday in range(1, 6):
        days.append(
            "<i>" + WEEKDAY_NAMES[weekday] + "</i>\n" + get_timetable(weekday, cur_week)
        )

    return days


def get_current_group(current_week: int) -> str:
    current_week = current_week % 3

    if current_week == 2:
        return "АЛЬФА"

    if current_week == 0:
        return "БЕТА"

    return "ГАММА"
