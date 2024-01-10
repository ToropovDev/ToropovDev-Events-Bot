import datetime

from database_functions.creating_tables import *
from random import randint
from google_sheets import *

# Добавление юзера
def add_user(user_id):
    cur.execute("SELECT * FROM users;")
    fetch_all = cur.fetchall()
    for user in fetch_all:
        if user[0] == user_id:
            return
    cur.execute("INSERT INTO users VALUES(?, ?);", (user_id, 0))
    conn.commit()

# Добавление сотрудника
def add_employee(user_id, name):
    cur.execute("SELECT * FROM employees;")
    fetch_all = cur.fetchall()
    for user in fetch_all:
        if user[0] == user_id:
            return
    cur.execute("INSERT INTO employees VALUES(?, ?);", (user_id, name))
    conn.commit()

# Создание нового админа
def make_admin(user_id):
    cur.execute("UPDATE users SET is_admin=1 WHERE id=(?)", (user_id, ))
    conn.commit()

# Добавление мероприятия
def add_event(event_info):
    cur.execute("SELECT * FROM events;")
    fetch_all_id = cur.fetchall()
    all_ids = [fetch_all_id[i][0] for i in range(len(fetch_all_id))]
    event_id = randint(100, 1000)
    if event_id in all_ids:
        while event_id in all_ids:
            event_id = randint(100, 1000)
    event_info[0] = event_id
    cur.execute("INSERT INTO events VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", tuple(event_info))
    conn.commit()
    return event_id

# Удаление мероприятия
def delete_event(event_id):
    cur.execute("DELETE FROM events WHERE eventid=?", (event_id,))
    conn.commit()

# Архивация меро
def archivate_event(event_id):
    cur.execute("SELECT * FROM events;")
    fetch_all = cur.fetchall()
    event_info = tuple()
    for event in fetch_all:
        if event[0] == int(event_id):
            event_info = event
    cur.execute("INSERT INTO archive VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", event_info)
    cur.execute("DELETE FROM events WHERE eventid=?", (event_id, ))
    conn.commit()
    add_event_to_archive_sheet(event_id)
    return True


async def auto_archivate():
    cur.execute("SELECT * FROM events;")
    fetch_all = cur.fetchall()
    for event in fetch_all:
        today = str(datetime.datetime.now()).split()[0].split('-')
        today = today[2] + '.' + today[1] + "." + today[0]
        print(event[3], today)
        if event[3] == today:
            archivate_event(event[0])



