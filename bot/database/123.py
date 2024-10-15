import asyncio

from clients_database import clients
from clients_telegram_database import clients_telegram
path = "C:\\Users\\admin\\Desktop\\ZenithBot\\ZenithBot\\bot\\database\\clients.csv"


async def update():
    await clients.create_table()
    await clients_telegram.create_table()
    await clients.update_table()


asyncio.run(update())