from aiogram.dispatcher.filters.state import State, StatesGroup

# КЛАССЫ СТЕЙТОВ
class AdminLogin(StatesGroup):
    waiting_for_admin_code = State()

class Login(StatesGroup):
    waiting_for_name = State()

class AddEvent(StatesGroup):
    waiting_for_name = State()
    waiting_for_cost = State()
    waiting_for_date = State()
    waiting_for_start_time = State()
    waiting_for_end_time = State()
    waiting_for_contacts = State()
    waiting_for_address = State()
    waiting_for_about = State()

class EventInfo(StatesGroup):
    waiting_for_id = State()

class Edit(StatesGroup):
    waiting_for_new_value = State()

class Mailing(StatesGroup):
    waiting_for_text = State()