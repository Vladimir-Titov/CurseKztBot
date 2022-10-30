import asyncpg


class DBRepository:

    def __init__(self, db_pool: asyncpg.Pool):
        self.db_pool = db_pool

