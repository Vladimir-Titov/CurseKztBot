import logging

from aiogram import Bot, Dispatcher

from settings import TelegramConfig

logging.basicConfig(level=logging.INFO)


def init_bot() -> Dispatcher:
    bot = Bot(token=TelegramConfig.BOT_TOKEN)
    dispatcher = Dispatcher(bot)
    return dispatcher


dp = init_bot()
