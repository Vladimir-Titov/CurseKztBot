import asyncio
from pprint import pprint

import aiohttp
from aiogram import types

from settings.telegram import TelegramConfig
from web import dp


async def get_status():
    async with aiohttp.ClientSession() as session:
        async with session.get(TelegramConfig.PASSPORT_URL) as response:
            pprint(await response.text())
            return None


@dp.message_handler(commands=['get_passport_status'])
async def get_passport_status(message: types.Message):
    status = await get_status()
    return message.answer(status)


if __name__ == '__main__':
    asyncio.run(get_status())
