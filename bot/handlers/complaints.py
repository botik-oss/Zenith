from aiogram import types, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from bot.core.config import TOKEN
from bot.core.constants import complaints
from bot.keyboards.menu import menu
from bot.handlers.fsm import Complaint_menu

router = Router()
bot = Bot(token=TOKEN)


async def accept_to_complaint(callback: types.CallbackQuery, state: FSMContext):
    # Установим состояние в Complaint_menu.complaint
    await state.set_state(Complaint_menu.complaint)
    menu.complaine_1()
    # Отправим меню menu.complaine_1()
    photo_03 = FSInputFile("Черный.jpg")
    await callback.message.answer_photo(photo_03, complaints[0],
                                        parse_mode='Markdown',
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))


async def make_complaint(callback: types.CallbackQuery, state=FSMContext):
    menu.complaine_2()
    photo_03 = FSInputFile("Черный.jpg")
    await callback.message.answer_photo(photo_03, complaints[1],
                                        parse_mode='Markdown',
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))
    if callback.data == "complaint_1":
        await state.set_state(Complaint_menu.action)


async def send_complaint(admin_id, message: types.Message, state=FSMContext):
    print(1)
    mes = "Жалоба: " + message.text
    photo_03 = FSInputFile("Черный.jpg")
    menu.complaine_1()
    await message.answer("Жалоба была отправлена!")
    await bot.send_message(admin_id, mes)
    await state.set_state(Complaint_menu.action)
    await message.answer_photo(photo_03, complaints[1],
                               parse_mode='Markdown',
                               reply_markup=menu.builder.as_markup(resize_keyboard=True))
