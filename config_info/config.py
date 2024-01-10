from aiogram import Bot, Dispatcher
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler


logging.basicConfig(level=logging.INFO)

bot = Bot(token="", parse_mode='HTML')
disp = Dispatcher(bot, storage=MemoryStorage())

admin_code = "2203"

scheduler = AsyncIOScheduler()

