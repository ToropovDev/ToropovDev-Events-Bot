from database_functions.main_db import *
from aiogram.dispatcher import FSMContext
from functions.states_classes import *
import keyboards as kb
from functions.self_logging import *

# ВХОД АДМИНА
@disp.callback_query_handler(text='login_admin')
async def admin_login(call: types.CallbackQuery, state: FSMContext):
    if check_admin(call.message.chat.id):
        await call.message.edit_text("🔓 Вы уже являетесь администратором!", reply_markup=kb.about_event_kb)
        return
    await call.message.edit_text("🔒 Введите код администратора")
    await state.set_state(AdminLogin.waiting_for_admin_code.state)

async def read_admin_code(message: types.Message, state: FSMContext):
    if message.text.lower() != admin_code:
        await message.answer("❌ Вы ввели неверный код!")
        return
    make_admin(message.from_user.id)
    await message.reply("Добро пожаловать! 😎\n\n‼️ Админ, помни! Для ввода любых "
                         "разделений (дата, время и т.д.) ВСЕГДА используется точка!", reply_markup=kb.about_event_kb)
    await log("Добавлен админ", message.from_user.id)
    await state.finish()

def register_handlers_admin_login(dp: disp):
    dp.register_message_handler(admin_login, commands='login', state="*")
    dp.register_message_handler(read_admin_code, state=AdminLogin.waiting_for_admin_code)

# ВХОД СОТРУДНИКА
@disp.callback_query_handler(text='login')
async def login(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите своё имя")
    await state.set_state(Login.waiting_for_name.state)

async def read_name(message: types.Message, state: FSMContext):
    add_employee(message.from_user.id, message.text)
    await message.reply("Добро пожаловать! 😎\n\n"
                        "Теперь ты можешь просматривать список мероприятий, в который ты участвуешь!", reply_markup=kb.all_events_kb)
    await log("Добавлен сотрудник", message.from_user.id)
    await state.finish()

def register_handlers_login(dp: disp):
    dp.register_message_handler(login, commands='login', state='*')
    dp.register_message_handler(read_name, state=Login.waiting_for_name)