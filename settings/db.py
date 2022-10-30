from .base import env


class DBConfig:
    DB_DSN = env.str('DB_DSN', 'postgresql://postgres:postgres@localhost:54320/curs_bot')
