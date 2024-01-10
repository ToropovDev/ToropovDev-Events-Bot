import datetime
from functions.self_logging import *
from aiogram import types
from config_info.config import *
from database_functions.get_info import get_event_datetime
from database_functions.main_db import *
from aiogram.dispatcher import FSMContext
from functions.states_classes import *
import keyboards as kb
from functions.notify import schedule_jobs

async def check_date(date):
    try:
        datetime.datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
        return 0
    return 1

# СОЗДАНИЕ МЕРОПРИЯТИЯ
@disp.callback_query_handler(text='new_event')
async def new_event(call: types.CallbackQuery, state: FSMContext):
    if not check_admin(call.message.chat.id):
        await call.message.edit_text("❌ Ваших прав недостаточно для выполнения данной команды!", reply_markup=kb.all_events_kb)
        return
    await call.message.edit_text("🖋 Введите название мероприятия")
    await state.set_state(AddEvent.waiting_for_name.state)

async def read_event_name(message: types.Message, state: FSMContext):
    await state.update_data(event_name=message.text)
    await message.answer("💵 Введите стоимость (без точек, запятых и пробелов")
    await state.set_state(AddEvent.waiting_for_cost.state)

async def read_event_cost(message: types.Message, state: FSMContext):
    await state.update_data(event_cost=int(message.text))
    await message.answer("🗓 Введите дату в формате ДД.ММ.ГГ")
    await state.set_state(AddEvent.waiting_for_date.state)

async def read_event_date(message: types.Message, state: FSMContext):
    input_date = str(message.text)
    input_date = input_date[:6] + "20" + input_date[6:]
    if not await check_date(input_date):
        await message.answer("❌ Введена некорректная дата!")
        return
    await state.update_data(event_date=input_date)
    await message.answer("🕗 Введите время начала мероприятия (через точку!)")
    await state.set_state(AddEvent.waiting_for_start_time.state)

async def read_event_start_time(message: types.Message, state: FSMContext):
    try:
        time = message.text.split('.')
        if not (-1 < int(time[0]) < 24 and -1 < int(time[1]) < 60):
            await message.answer("❌ Введено некорректное время!")
            return
    except ValueError:
        await message.answer("❌ Введено некорректное время!")
        return

    await state.update_data(event_start_time=message.text)
    await message.answer("🕗 Введите время окончания мероприятия")
    await state.set_state(AddEvent.waiting_for_end_time.state)

async def read_event_end_time(message: types.Message, state: FSMContext):
    try:
        time = message.text.split('.')
        if not (-1 < int(time[0]) < 24 and -1 < int(time[1]) < 60):
            await message.answer("❌ Введено некорректное время!")
            return
    except ValueError:
        await message.answer("❌ Введено некорректное время!")
        return
    await state.update_data(event_end_time=message.text)
    await message.answer("☎️ Введите контакты")
    print(1)
    await state.set_state(AddEvent.waiting_for_contacts.state)

async def read_event_contacts(message: types.Message, state: FSMContext):
    await state.update_data(event_contacts=message.text)
    await message.answer("📍 Введите адрес")
    print(2)
    await state.set_state(AddEvent.waiting_for_address.state)
async def read_event_address(message: types.Message, state: FSMContext):
    await state.update_data(event_address=message.text)
    await message.answer("🖋 Введите описание")
    await state.set_state(AddEvent.waiting_for_about.state)

async def read_event_about(message: types.Message, state: FSMContext):
    await state.update_data(event_about=message.text)
    data = await state.get_data()
    event_info = [0, data['event_name'],
                  data['event_cost'],
                  data['event_date'],
                  data['event_start_time'],
                  data['event_end_time'],
                  data['event_contacts'],
                  data['event_address'],
                  data['event_about']
                  ]
    event_id = add_event(event_info)
    await state.finish()
    await message.reply("Мероприятие добавлено! 🥳\n\n\n"
                         f"<b>{event_info[1]}</b> - 💵 {event_info[2]} рублей\n\n"
                         f"🗓 {event_info[3]}, "
                         f"🕗 {event_info[4]}-{event_info[5]}\n\n"
                         f"☎️ {event_info[6]}\n\n"
                         f"📍 {event_info[7]}\n\n"
                         f"ℹ️ {event_info[8]}\n\n"
                         f"🆔 ID мероприятия: {event_id}",
                        reply_markup=kb.about_event_kb)
    await log("Добавлено новое мероприятие", message.from_user.id)
    await schedule_jobs(get_event_datetime(event_id), event_id)

def register_handlers_new_event(dp: disp):
    dp.register_message_handler(new_event, commands='new_event', state="*")
    dp.register_message_handler(read_event_name, state=AddEvent.waiting_for_name)
    dp.register_message_handler(read_event_cost, state=AddEvent.waiting_for_cost)
    dp.register_message_handler(read_event_date, state=AddEvent.waiting_for_date)
    dp.register_message_handler(read_event_start_time, state=AddEvent.waiting_for_start_time)
    dp.register_message_handler(read_event_end_time, state=AddEvent.waiting_for_end_time)
    dp.register_message_handler(read_event_contacts, state=AddEvent.waiting_for_contacts)
    dp.register_message_handler(read_event_address, state=AddEvent.waiting_for_address)
    dp.register_message_handler(read_event_about, state=AddEvent.waiting_for_about)


