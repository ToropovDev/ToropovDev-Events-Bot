from database_functions.get_info import *
from database_functions.main_db import *
import keyboards as kb
from google_sheets import *
from functions.self_logging import *

# АРХИВАЦИЯ МЕРОПРИЯТИЯ
@disp.callback_query_handler(text="to_archive")
async def to_archive(call: types.CallbackQuery):
    if not check_admin(call.message.chat.id):
        await call.message.edit_text("❌ Ваших прав недостаточно для выполнения данной команды!",
                                     reply_markup=kb.all_events_kb)
        return
    event_id = call.message.text.split()[-1]
    print(event_id)
    archivate_event(event_id)
    text = get_all_events()[0]
    await log("Архивировано мероприятие", call.message.chat.id)
    await call.message.edit_text(text, reply_markup=kb.all_events_buttons(get_all_events()[1]))


@disp.callback_query_handler(text='view_archive')
async def view_archive(call: types.CallbackQuery):
    text = get_all_archive()
    await call.message.edit_text(text, reply_markup=kb.all_events_kb)
    await log("Просмотрен архив", call.message.chat.id)
