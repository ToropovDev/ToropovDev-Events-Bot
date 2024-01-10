from database_functions.get_info import *
from functions.states_classes import *
import keyboards as kb
from functions.self_logging import *

# СПИСОК ВСЕХ МЕРОПРИЯТИЙ
ids = []

@disp.callback_query_handler(text='all_events')
async def all_events(call: types.CallbackQuery):
    text, events = get_all_events()
    global ids
    for elem in get_events_ids():
        if elem[0] not in ids:
            ids += [elem[0]]
    await log("Список всех мероприятий", call.message.chat.id)
    await call.message.edit_text(text, reply_markup=kb.all_events_buttons(events))

@disp.callback_query_handler(text=ids)
async def send_event_info(call: types.CallbackQuery):
    await call.message.edit_text(get_event_info(call.get_current().data), reply_markup=kb.in_event_kb)

def register_handlers_all_events(dp: disp):
    dp.register_message_handler(all_events, commands='all_events', state='*')
    dp.register_message_handler(send_event_info, state=EventInfo.waiting_for_id)
