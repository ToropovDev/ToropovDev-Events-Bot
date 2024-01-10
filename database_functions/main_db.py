from database_functions.edit_info import *

# Проверка юзера на админа
def check_admin(user_id):
    cur.execute("SELECT * FROM users;")
    fetch_all = cur.fetchall()
    for user in fetch_all:
        if user[0] == user_id:
            return user[1]
    return 0

# Обновление параметра
def update_param_value(event_id, param_index, new_value):
    match param_index:
        case 0:
            cur.execute('''UPDATE events SET event_name=? WHERE eventid=?''', (new_value, event_id))
        case 1:
            cur.execute('''UPDATE events SET event_cost=? WHERE eventid=?''', (new_value, event_id))
        case 2:
            cur.execute('''UPDATE events SET event_date=? WHERE eventid=?''', (new_value, event_id))
        case 3:
            cur.execute('''UPDATE events SET start_time=? WHERE eventid=?''', (new_value, event_id))
        case 4:
            cur.execute('''UPDATE events SET end_time=? WHERE eventid=?''', (new_value, event_id))
        case 5:
            cur.execute('''UPDATE events SET contacts=? WHERE eventid=?''', (new_value, event_id))
        case 6:
            cur.execute('''UPDATE events SET address=? WHERE eventid=?''', (new_value, event_id))
        case 7:
            cur.execute('''UPDATE events SET about=? WHERE eventid=?''', (new_value, event_id))

    conn.commit()


