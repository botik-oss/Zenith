from aiogram import types, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from core.constants import complaints
from keyboards.menu import menu
from fsm.states import Complaint_menu

router = Router()
TOKEN = '7536990395:AAFpT5VXsx0VuBuqoG5ha7h5pzeBQCIG1SM'
bot = Bot(token=TOKEN)
admin_id = "1795780447"


@router.callback_query(Complaint_menu.action)
async def complaint_menu_1(callback: types.CallbackQuery, state=FSMContext):
    # Установим состояние в Complaint_menu.complaint
    await state.set_state(Complaint_menu.complaint)
    menu.complaine_1()
    # Отправим меню menu.complaine_1()
    photo_03 = FSInputFile("Черный.jpg")
    await callback.message.answer_photo(photo_03, complaints[0],
                                        parse_mode='Markdown',
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))


@router.callback_query(Complaint_menu.complaint)
async def complaint_menu_2(callback: types.CallbackQuery, state=FSMContext):
    menu.complaine_2()
    photo_03 = FSInputFile("Черный.jpg")
    await callback.message.answer_photo(photo_03, complaints[1],
                                        parse_mode='Markdown',
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))
    if callback.data == "complaint_1":
        await state.set_state(Complaint_menu.action)


@router.message(Complaint_menu.complaint)
async def send_complaint_to_admin(admin_id, message: types.Message, state=FSMContext):
    mes = "Жалоба: " + message.text
    photo_03 = FSInputFile("Черный.jpg")
    menu.complaine_1()
    await message.answer("Жалоба была отправлена!")
    await bot.send_message(admin_id, mes)
    await state.set_state(Complaint_menu.action)
    await message.answer_photo(photo_03, complaints[1],
                               parse_mode='Markdown',
                               reply_markup=menu.builder.as_markup(resize_keyboard=True))
