from .base import env


class ExchangeConfig:
    URL = env.str('URL_EXCHANGE', '')
    RUB = env.str('RUB', '643')
    KZT = env.str('KZT', '398')
