from aiogram import types

from web import dp
from app.curs import get_kzt_curs
from emoji import emojize


async def format_message(curs: str) -> str:
    rub = emojize(":Russia:")
    kzt = emojize(":Kazakhstan:")
    curs = 100 / (float(curs) * 100)
    return f'Курс на сегодня {rub} => {kzt} = {round(curs, 2)}'


@dp.message_handler(commands=['curs', 'curs_kzt'])
async def get_kzt_curs_handler(message: types.Message):
    curs = await get_kzt_curs()
    format_text = await format_message(curs)
    await message.answer(format_text)
