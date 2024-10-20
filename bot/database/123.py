import asyncio

from admins_database import admins


async def fadsf():
    await admins.add_new_admin(1041359456)


asyncio.run(fadsf())
