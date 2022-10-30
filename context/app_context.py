import logging

import asyncpg
from aiogram import Dispatcher

from settings.db import DBConfig

logger = logging.getLogger(__name__)


async def on_startup(dispatcher: Dispatcher):
    bot = dispatcher.bot
    logger.info('open pool connection')
    bot['db_pool'] = await asyncpg.create_pool(dsn=DBConfig.DB_DSN)


async def on_shutdown(dispatcher: Dispatcher):
    bot = dispatcher.bot
    logger.info('close pool connection')
    await bot['db_pool'].close()
