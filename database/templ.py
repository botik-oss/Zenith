import csv
import sqlite3

conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        client_number INTEGER,
        name TEXT,
        gender TEXT,
        date_of_birth TEXT
    )
''')

#TODO обработка файла
#TODO точность полей
#TODO валидация данных
#TODO методы получения данных

with open('clients.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) #пропускаем заголовок
    for row in reader:
        client_number, name, gender, date_of_birth, mark, appendix = row
        if mark:
            continue
        cursor.execute('''
            INSERT INTO clients (client_number, name, gender, date_of_birth)
            VALUES (?, ?, ?, ?)
        ''', (client_number, name, gender, date_of_birth))

conn.commit()
conn.close()
