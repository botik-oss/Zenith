from aiogram import types
from aiogram.types import FSInputFile
from bot.keyboards.menu import menu
from bot.core.constants import question


def add_button(text):
    button_number = len(menu.question_buttons) - 1
    button_callback = "new_button" + str(button_number)
    menu.new_button(text, button_callback)


async def ask_question(callback: types.CallbackQuery):
    menu.question()
    photo_02 = FSInputFile("Черный.jpg")
    await callback.message.answer_photo(photo_02, question,
                    parse_mode='Markdown', reply_markup=menu.builder.as_markup(resize_keyboard=True))

