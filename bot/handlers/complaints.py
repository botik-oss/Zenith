from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from bot.core.constants import complaints
from bot.keyboards.menu import menu
from bot.fsm.states import Complaint_menu
from bot.core.config import MAIN_ADMIN_ID
from bot.core import config
from aiogram import types, Router, F, Bot

TOKEN = config.TOKEN
bot = Bot(token=TOKEN)

router = Router()
admin_id = MAIN_ADMIN_ID


@router.callback_query(F.data == "complaint_1")
async def complaint_menu_1(callback: types.CallbackQuery):
    menu.complaint_1()
    # Отправим меню menu.complaine_1()
    photo_03 = FSInputFile("Черный.jpg")
    await callback.message.answer_photo(photo_03, complaints[0],
                                        parse_mode='Markdown',
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))


@router.callback_query(F.data == "complaint_2")
async def complaint_menu_2(callback: types.CallbackQuery, state=FSMContext):
    menu.complaint_2()
    photo_03 = FSInputFile("Черный.jpg")
    await callback.message.answer_photo(photo_03, complaints[1],
                                        parse_mode='Markdown',
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))
    await state.set_state(Complaint_menu.complaint)


@router.message(Complaint_menu.complaint)
async def send_complaint_to_admin(message: types.Message, state=FSMContext):
    photo_03 = FSInputFile("Черный.jpg")
    mes = "Жалоба: " + message.text
    await message.answer("Жалоба была отправлена!")
    await bot.send_message(admin_id, mes)
    await message.answer_photo(photo_03, complaints[1],
                                        parse_mode='Markdown',
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))
