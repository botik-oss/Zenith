import csv
import sqlite3
from core import constants
from clients_telegram_database import ClientsTelegramDatabase

CLIENTS_DATABASE = constants.clients_database
TABLE_NAME = "clients"


class ClientsDatabase:

    def __init__(self) -> None:
        self.connection = sqlite3.connect(f'{CLIENTS_DATABASE}')
        self.cursor = self.connection.cursor()

    def create_table(self) -> None:
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                client_number INTEGER,
                name TEXT,
                gender TEXT,
                date_of_birth TEXT
            )
        ''')
        self.connection.commit()

    def update_table(self, path: str) -> None:
        try:
            with open(f'{path}', 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # пропускаем заголовок
                clients_telegram = ClientsTelegramDatabase()
                for row in reader:
                    client_number, name, gender, date_of_birth, mark, appendix = row
                    if mark:
                        if clients_telegram.check_client_exist(client_number):
                            clients_telegram.remove_client(client_number)
                        continue
                    self.cursor.execute(f'''
                        INSERT INTO {TABLE_NAME} (client_number, name, gender, date_of_birth)
                        VALUES (?, ?, ?, ?)
                    ''', (client_number, name, gender, date_of_birth))
        except Exception:
            raise Exception("Ошибка при обновлении базы данных")
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
