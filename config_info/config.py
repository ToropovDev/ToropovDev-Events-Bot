from aiogram import Bot, Dispatcher
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler


logging.basicConfig(level=logging.INFO)

bot = Bot(token="6529521284:AAEVRxgL6nRkbwMcGzxOxx8lhOm7kW7h3R4", parse_mode='HTML')
disp = Dispatcher(bot, storage=MemoryStorage())

admin_code = "2203"

scheduler = AsyncIOScheduler()

