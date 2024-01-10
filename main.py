import asyncio
from functions.auth import *
from functions.add_event import *
from functions.edit import *
from functions.all_events import *
from functions.archive import *
from functions.mailing import *


# ЗАПУСК БОТА
@disp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    add_user(message.from_user.id)
    await message.reply("Привет!👋\n\nЭто бот для управления мероприятиями Зелёных Человечков."
                        "Ты можешь войти как админ, чтобы создавать записи о мероприятиях и отмечать ответственных, "
                        "либо как сотрудник, чтобы знать, в каких мероприятиях ты принимаешь участие!"
                        "\n\n<b>GreenTeamManager, v1.2 от 13.05.2023</b>",
                        reply_markup=kb.login_kb)


async def main():
    register_handlers_admin_login(disp)
    register_handlers_new_event(disp)
    register_handlers_all_events(disp)
    register_handlers_edit(disp)
    register_handlers_login(disp)
    register_handlers_all_events(disp)

    scheduler.start()
    scheduler.add_job(auto_archivate, "cron", hour=23, minute=55)
    await disp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
