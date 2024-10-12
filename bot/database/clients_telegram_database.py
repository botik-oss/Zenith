import aiosqlite

from core import constants

CLIENTS_DATABASE = constants.clients_database
TABLE_NAME = "clients_telegram"


class ClientsTelegramDatabase:

    def __init__(self) -> None:
        self.database_path = CLIENTS_DATABASE

    async def create_table(self) -> None:
        async with aiosqlite.connect(self.database_path) as connection:
            await connection.execute('''
                CREATE TABLE IF NOT EXISTS clients_telegram (
                    client_number INTEGER,
                    telegram_id INTEGER,
                    telegram_username TEXT
                )
            ''')
            await connection.execute(f'''
                CREATE INDEX IF NOT EXISTS idx_clients_telegram_client_number ON clients_telegram(client_number)
            ''')
            await connection.commit()

    async def add_client(self, client_number: int, telegram_id: str, telegram_username: str) -> None:
        async with aiosqlite.connect(self.database_path) as connection:
            await connection.execute(f'''
                INSERT INTO {TABLE_NAME} (client_number, telegram_id, telegram_username)
                VALUES (?, ?, ?)
            ''', (client_number, telegram_id, telegram_username))
            await connection.commit()

    async def remove_client(self, client_number: int, cursor: any) -> None:
        await cursor.execute(f'''
                DELETE FROM {TABLE_NAME} WHERE client_number = ?
            ''', (client_number,))

    async def check_client_exist(self, client_number: int) -> bool:
        async with aiosqlite.connect(self.database_path) as connection:
            async with connection.execute(f'''
                SELECT 1 FROM {TABLE_NAME} WHERE client_number = ?
            ''', (client_number,)) as cursor:
                return await cursor.fetchone() is not None
