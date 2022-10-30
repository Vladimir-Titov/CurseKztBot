from aiogram import executor
from context import on_shutdown, on_startup

from web import dp

if __name__ == '__main__':
    import app.handlers
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
