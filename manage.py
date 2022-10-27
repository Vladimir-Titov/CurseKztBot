from aiogram import executor, types

from web.initializers import dp

if __name__ == '__main__':
    import app.handlers

    executor.start_polling(dp, skip_updates=True)
