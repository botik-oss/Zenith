from aiogram import types
from aiogram.types import FSInputFile

from bot.core.constants import complaints
from bot.keyboards.menu import menu


async def complaints_1(callback: types.CallbackQuery):
    menu.complaine_1()
    photo_03 = FSInputFile("Черный.jpg")

    await callback.message.answer_photo(photo_03, complaints[0],
        parse_mode='Markdown', reply_markup=menu.builder.as_markup(resize_keyboard=True))


async def complaints_2(callback: types.CallbackQuery):
    menu.complaine_2()
    photo_03 = FSInputFile("Черный.jpg")

    await callback.message.answer_photo(photo_03, complaints[1],
        parse_mode='Markdown', reply_markup=menu.builder.as_markup(resize_keyboard=True))