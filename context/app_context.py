import logging
import sqlite3
from app.sql import create_table
from aiogram import Dispatcher

from settings.db import DBConfig

logger = logging.getLogger(__name__)


async def on_startup(dispatcher: Dispatcher):
    bot = dispatcher.bot
    logger.info('open pool connection')
    with sqlite3.connect(DBConfig.DB_NAME) as conn:
        bot['db_pool'] = conn
        bot['db_pool'].executescript(create_table)


async def on_shutdown(dispatcher: Dispatcher):
    bot = dispatcher.bot
    logger.info('close pool connection')
    bot['db_pool'].close()
