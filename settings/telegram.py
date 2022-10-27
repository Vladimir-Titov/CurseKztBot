from .base import env


class TelegramConfig:
    BOT_TOKEN = env.str('TELEGRAM_TOKEN', '')
    HELLO_MESSAGE = env.str('HELLO_MESSAGE', '')
