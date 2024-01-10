from aiogram import types
from config_info.config import *
from database_functions.get_info import get_admins_ids


async def log(text, user_id):
    with open('config_info/logging_flag.txt', 'r') as file:
        if int(file.read()) == 1:
            await bot.send_message(705533785, "log: Новое действие! \n\n"
                                              f"by {user_id}\n"
                                              f"event: {text}")


@disp.message_handler(commands=['logging_on'])
async def turn_logging_on(message: types.Message):
    with open('config_info/logging_flag.txt', 'w') as file:
        file.write('1')
    await bot.send_message(705533785, "Логирование включено!")


@disp.message_handler(commands=['logging_off'])
async def turn_logging_off(message: types.Message):
    with open('config_info/logging_flag.txt', 'w') as file:
        file.write('0')
    await bot.send_message(705533785, "Логирование выключено!")


