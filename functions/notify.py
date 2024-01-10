from config_info.config import *
import keyboards as kb
from database_functions.get_info import *


# Планирование задач
async def schedule_jobs(date, event_id):
    scheduler.add_job(one_day_notify, "date", run_date=date - datetime.timedelta(1), args=(event_id, ))
    scheduler.add_job(three_day_notify, "date", run_date=date - datetime.timedelta(3), args=(event_id, ))


# Уведомления о приближающемся мероприятии
async def one_day_notify(event_id):
    for admin_id in get_admins_ids():
        await bot.send_message(admin_id, f"Уже завтра состоится мероприятие! 🥳 \n\n{get_event_info(event_id)}️",
                               reply_markup=kb.all_events_kb)

def three_day_notify(event_id):
    for admin_id in get_admins_ids():
        bot.send_message(admin_id, f"Через 3 дня мероприятие! 🥳 \n\n{get_event_info(event_id)}️",
                               reply_markup=kb.all_events_kb)