import logging

from aiogram import Bot, Dispatcher

from settings import TelegramConfig

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TelegramConfig.BOT_TOKEN)
dp = Dispatcher(bot)
