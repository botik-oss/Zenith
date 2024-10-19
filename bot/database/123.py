import asyncio

from admins_database import admins


async def fadsf():
    await admins.create_table()
    await admins.add_new_admin(934192145)


asyncio.run(fadsf())
