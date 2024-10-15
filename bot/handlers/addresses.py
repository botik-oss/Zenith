from aiogram import types
from core.constants import adress
from aiogram.types import FSInputFile

from core.constants import adress
from keyboards.menu import menu


async def adresses(callback: types.CallbackQuery):
    menu.back_to_menu()
    photo_03 = FSInputFile("Черный.jpg")

    await callback.message.answer_photo(photo_03, adress,
                                        parse_mode='Markdown',
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))
