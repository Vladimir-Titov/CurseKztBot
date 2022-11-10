from .base import env


class DBConfig:
    DB_URL = env.str('DB_URL', 'postgresql://postgres:postgres@localhost:54320/postgres')
    DB_NAME = env.str('DB_NAME', 'curs_bot.db')
