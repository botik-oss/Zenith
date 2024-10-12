from aiogram import types
from ZenithBot.bot.core.constants import adress


async def adresses(callback: types.CallbackQuery):
    await callback.message.answer(adress,
        parse_mode='Markdown'
    )