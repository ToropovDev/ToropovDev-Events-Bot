from database_functions.creating_tables import *
import datetime

# Получение информации о мероприятии в тексте для отправки
def get_event_info(event_id):
    cur.execute("SELECT * FROM events;")
    fetch_all = cur.fetchall()
    event_info = []
    for event in fetch_all:
        if event[0] == int(event_id):
            event_info = list(event)
    result = "Информация о мероприятии!\n\n\n" \
    f"<b>{event_info[1]}</b> - 💵 {event_info[2]} рублей\n\n" \
    f"🗓 {event_info[3]}, " \
    f"🕗 {event_info[4]}-{event_info[5]}\n\n" \
    f"ℹ☎️ {event_info[6]}\n\n" \
     f"ℹ📍 {event_info[7]}\n\n" \
     f"ℹ️ {event_info[8]}\n\n" \
    f"🆔 ID мероприятия: {event_id}"
    return result

# получение списка айди админов
def get_admins_ids():
    cur.execute("SELECT id FROM users WHERE is_admin=1;")
    fetch_all = cur.fetchall()
    result = [i[0] for i in fetch_all]
    return result

def get_all_ids():
    cur.execute("SELECT id FROM users;")
    fetch_all = cur.fetchall()
    result = [i[0] for i in fetch_all]
    return result

# Получение параметра мероприятия
def get_event_param(event_id, param_index):
    cur.execute("SELECT * FROM events;")
    fetch_all = cur.fetchall()
    result = ''
    for event in fetch_all:
        if event[0] == event_id:
            result = str(event[param_index+1])
    return result

def get_event_info_list(event_id):
    cur.execute("SELECT * FROM archive;")
    fetch_all = cur.fetchall()
    event_id = int(event_id)
    result = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    for event in fetch_all:
        if event[0] == event_id:
            result = event
    return result


# Получение инфы о всех меро в виде текста
def get_all_events():
    cur.execute("SELECT * FROM events;")
    fetch_all = cur.fetchall()
    result = "<b>Все мероприятия:</b>\n\n"
    events = []
    for i in range(len(fetch_all)):
        events += [(fetch_all[i][1], fetch_all[i][0], fetch_all[i][3].split("."))]
    events = sorted(events, key=lambda x: (x[2][2], x[2][1], x[2][0]))
    for i in range(len(events)):
        result += f"{i+1}) {events[i][0]} (ID: {events[i][1]})\n" \
                  f"🗓 Дата: {events[i][2][0]+'.'+events[i][2][1]+'.'+events[i][2][2]}\n\n"
    result += "\n❕ Посмотреть подробную информацию:"
    if not events:
        result = "Нет запланированных мероприятий!"
    return result, events

# получение инфы о всех меро в архиве в виде текста
def get_all_archive():
    cur.execute("SELECT * FROM archive;")
    fetch_all = cur.fetchall()
    result = "<b>Архив мероприятий</b>\n\n" \
             "Посмотреть подробную информацию об архивных мероприятиях можно в " \
             "<a href=\"https://docs.google.com/spreadsheets/d" \
             "/1Co-Rv7WeCT_RYQM7U14PRBb8EQBhLed1sSXD84OPBrE/edit#gid=0\">таблице</a>\n\n"
    events = []
    for i in range(len(fetch_all)):
        events += [(fetch_all[i][1], fetch_all[i][0], fetch_all[i][3].split("."))]
    events = sorted(events, key=lambda x: (x[2][2], x[2][1], x[2][0]))
    for i in range(len(events)):
        result += f"{i+1}) {events[i][0]} (ID: {events[i][1]})\n" \
                  f"🗓 Дата: {events[i][2][0]+'.'+events[i][2][1]+'.'+events[i][2][2]}\n\n"
    return result

# Получение ID всех меро
def get_events_ids():
    cur.execute("SELECT * FROM events;")
    fetch_all = cur.fetchall()
    result = []
    for i in range(len(fetch_all)):
        result += [(fetch_all[i][0], fetch_all[i][1])]
    return result

# Получение даты и времени меро
def get_event_datetime(event_id):
    cur.execute("SELECT * FROM events;")
    fetch_all = cur.fetchall()
    date, time = '', ''
    for event in fetch_all:
        if event[0] == event_id:
            date = event[3].split('.')
            time = event[4].split('.')
    result = datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]))
    return result
