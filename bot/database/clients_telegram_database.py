import csv
import sqlite3
from core import constants

CLIENTS_DATABASE = constants.clients_database
TABLE_NAME = "clients_telegram"


class ClientsTelegramDatabase:

    def __init__(self) -> None:
        self.connection = sqlite3.connect(f'{CLIENTS_DATABASE}')
        self.cursor = self.connection.cursor()

    def create_table(self) -> None:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients_telegram (
                client_number INTEGER,
                telegram_id TEXT,
                telegram_username TEXT
            )
        ''')
        self.connection.commit()

    def add_client(self, client_number: int, telegram_id: str, telegram_username: str) -> None:
        self.cursor.execute(f'''
            INSERT INTO {TABLE_NAME} (client_number, telegram_id, telegram_username)
            VALUES (?, ?, ?)
        ''', (client_number, telegram_id, telegram_username))
        self.connection.commit()

    def remove_client(self, client_number: int) -> None:
        self.cursor.execute(f'''
                    DELETE FROM {TABLE_NAME} WHERE client_number = ?
                ''', (client_number,))
        self.connection.commit()

    def check_client_exist(self, client_number: int) -> bool:
        self.cursor.execute(f'''
            SELECT 1 FROM {TABLE_NAME} WHERE client_number = ?
        ''', (client_number,))
        return self.cursor.fetchone() is not None

    def close(self) -> None:
        self.connection.close()
