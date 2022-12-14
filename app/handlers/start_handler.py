from aiogram import types

from settings.telegram import TelegramConfig
from web import dp


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    print(message.bot['db_pool'])
    await message.reply(TelegramConfig.HELLO_MESSAGE)
