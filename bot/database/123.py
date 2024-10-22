import asyncio

from admins_database import admins
from clients_database import clients
from clients_telegram_database import clients_telegram


async def fadsf():
    print(await clients_telegram.get_all_clients_id())


asyncio.run(fadsf())
