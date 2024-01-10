import sqlite3

conn = sqlite3.connect("events.db")
cur = conn.cursor()

# Создание таблицы мероприятий
cur.execute("""CREATE TABLE IF NOT EXISTS events(
    eventid INT PRIMARY KEY,
    event_name TEXT,
    event_cost INT,
    event_date TEXT,
    start_time TEXT,
    end_time TEXT, 
    contacts TEXT, 
    address TEXT,
    about TEXT);
""")
conn.commit()

# Создание таблицы пользователей
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id INT PRIMARY KEY, 
    is_admin INT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS employees(
    id INT PRIMARY KEY, 
    name TEXT);
""")
conn.commit()

# Создание таблицы архива
cur.execute("""CREATE TABLE IF NOT EXISTS archive(
    eventid INT PRIMARY KEY,
    event_name TEXT,
    event_cost INT,
    event_date TEXT,
    start_time TEXT,
    end_time TEXT, 
    contacts TEXT,
    address TEXT,
    about TEXT);
""")
conn.commit()