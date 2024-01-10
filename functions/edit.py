from database_functions.get_info import *
from database_functions.main_db import *
from aiogram.dispatcher import FSMContext
from functions.self_logging import *
from functions.states_classes import *
import keyboards as kb
from database_functions.edit_info import *

# РЕДАКТИРОВАНИЕ ПАРАМЕТРОВ
@disp.callback_query_handler(text='edit')
async def get_param_to_edit(call: types.CallbackQuery, state: FSMContext):
    if not check_admin(call.message.chat.id):
        await call.message.edit_text("❌ Ваших прав недостаточно для выполнения данной команды!", reply_markup=kb.all_events_kb)
        return
    await state.update_data(id=call.message.text.split()[-1])
    await call.message.edit_text("Выберите, какой параметр нужно изменить: ", reply_markup=kb.get_params())

params = ['param0', 'param1', 'param2', 'param3', 'param4', 'param5', 'param6', 'param7']

@disp.callback_query_handler(text=params)
async def edit_param(call: types.CallbackQuery, state: FSMContext):
    event_id = int(dict(await state.get_data())['id'])
    await call.message.edit_text("❕ Значение в настоящий момент:")
    param_index = int(call.data[-1])
    await state.update_data(param_index=param_index)
    await call.message.answer(f"▶️ {get_event_param(event_id, param_index)}")
    await call.message.answer("Введите новое значение")
    await state.set_state(Edit.waiting_for_new_value.state)

async def read_new_value(message: types.Message, state: FSMContext):
    state_data = dict(await state.get_data())
    update_param_value(int(state_data['id']), int(state_data['param_index']), message.text)
    await message.answer("Значение изменено! 🥳", reply_markup=kb.all_events_kb)
    await state.finish()

def register_handlers_edit(dp: disp):
    dp.register_message_handler(edit_param, commands='edit', state="*")
    dp.register_message_handler(read_new_value, state=Edit.waiting_for_new_value)

# УДАЛЕНИЕ МЕРОПРИЯТИЯ
@disp.callback_query_handler(text="delete")
async def delete(call: types.CallbackQuery):
    event_id = call.message.text.split()[-1]
    delete_event(event_id)
    await log("Добавлено новое мероприятие", call.message.chat.id)
    await call.message.edit_text('Мероприятие удалено!', reply_markup=kb.all_events_kb)