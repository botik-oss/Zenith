from aiogram import types
from aiogram.types import FSInputFile

from core.constants import contact
from keyboards.menu import menu


async def contacts(callback: types.CallbackQuery):
    menu.back_to_menu()
    photo_07 = FSInputFile("static/contact_menu.png")
    await callback.message.answer_photo(photo_07, contact,
                                        parse_mode='Markdown', reply_markup=menu.builder.as_markup(resize_keyboard=True)
                                        )