from aiogram import types
from core.constants import contact

async def contacts(callback: types.CallbackQuery):
    await callback.message.answer(contact,
        parse_mode='Markdown'
    )