from main import *

@disp.message_handler(commands=['mailing'])
async def start_mailing(message: types.Message, state: FSMContext):
    print(1)
    await bot.send_message(705533785, "Введите текст рассылки")
    await state.set_state(Mailing.waiting_for_text.state)

async def do_mailing(message: types.Message, state: FSMContext):
    user_ids = get_all_ids()
    for user_id in user_ids:
        await bot.send_message(user_id, message.text)
    await bot.send_message(705533785, "Рассылка отправлена!")
    await state.finish()

def register_handlers_all_events(dp: disp):
    dp.register_message_handler(start_mailing, commands='all_events', state='*')
    dp.register_message_handler(do_mailing, state=Mailing.waiting_for_text)
