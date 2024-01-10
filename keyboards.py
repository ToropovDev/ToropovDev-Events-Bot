from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database_functions.get_info import *

# Кнопки
admin_login_btn = InlineKeyboardButton("Войти как администратор 😎", callback_data="login_admin")
login_btn = InlineKeyboardButton("Войти", callback_data="login")
new_event_btn = InlineKeyboardButton("Создать новое мероприятие ✍️", callback_data="new_event")
all_events_btn = InlineKeyboardButton("Все мероприятия 📋", callback_data="all_events")
edit_params_btn = InlineKeyboardButton("Редактировать ✏️", callback_data='edit')
archive_event_btn = InlineKeyboardButton("В архив 🗄", callback_data='to_archive')
view_archive_btn = InlineKeyboardButton("Посмотреть архив", callback_data="view_archive")
delete_event_btn = InlineKeyboardButton("Удалить ❌", callback_data='delete')

# Клавиатуры
login_kb = InlineKeyboardMarkup()\
    .add(login_btn)\
    .add(admin_login_btn)

all_events_kb = InlineKeyboardMarkup()\
    .add(all_events_btn)

about_event_kb = InlineKeyboardMarkup()\
    .add(new_event_btn)\
    .add(all_events_btn)

in_event_kb = InlineKeyboardMarkup()\
    .add(edit_params_btn)\
    .add(archive_event_btn)\
    .add(delete_event_btn)\
    .add(all_events_btn)


# Кнопки в списке всех мероприятий
def all_events_buttons(events):
    ids = [[event[0], event[1]] for event in events]
    num_of_events = len(ids)
    result = InlineKeyboardMarkup()
    for i in range(1, num_of_events + 1):
        exec(f"event{i} = InlineKeyboardButton('▶️ {ids[i-1][0]}', callback_data='{ids[i-1][1]}')")
        exec(f"result.add(event{i})")
    result.add(view_archive_btn)
    result.add(new_event_btn)
    return result

# Получение параметров
def get_params():
    result = InlineKeyboardMarkup()
    params = ['Название', "Стоимость", "Дата", "Время начала", "Время окончания", "Контакты", "Адрес", "Описание"]
    for i in range(len(params)):
        exec(f"param{i} = InlineKeyboardButton('{params[i]}', callback_data='param{i}')")
        exec(f"result.add(param{i})")
    back_btn = InlineKeyboardButton("Назад", callback_data="all_events")
    result.add(back_btn)
    return result
