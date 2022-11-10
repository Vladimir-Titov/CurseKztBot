from aiogram import types

from web import dp
from app.curs import get_kzt_curs
from emoji import emojize
from app.sql import insert_query, select_5, select_all

rub = emojize(":Russia:")
kzt = emojize(":Kazakhstan:")


async def format_message(curs: str) -> str:
    curs = 100 / (float(curs) * 100)
    return f"Курс на сегодня {rub} => {kzt} = {round(curs, 2)}"


@dp.message_handler(commands=["curs", "curs_kzt"])
async def get_kzt_curs_handler(message: types.Message):
    curs = await get_kzt_curs()
    curs_to_db = 100 / (float(curs) * 100)
    message.bot['db_pool'].execute(insert_query, [curs_to_db])
    message.bot['db_pool'].commit()
    format_text = await format_message(curs)
    await message.answer(format_text)


@dp.message_handler(commands=["history"])
async def history(message: types.Message):
    messages = []
    records = message.bot['db_pool'].cursor().execute(select_5)
    for row in records.fetchall():
        messages.append(f"Курс на {row[2]} {rub} => {kzt} = {round(row[1], 2)}")
    await message.answer(text='\n'.join(messages))


@dp.message_handler(commands=['all_history'])
async def all_history(message: types.Message):
    messages = []
    records = message.bot['db_pool'].cursor().execute(select_all)
    for row in records.fetchall():
        messages.append(f"Курс на {row[2]} {rub} => {kzt} = {round(row[1], 2)}")
    await message.answer(text='\n'.join(messages))
