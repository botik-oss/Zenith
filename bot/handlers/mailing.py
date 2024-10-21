from aiogram.fsm.context import FSMContext

from aiogram import types, Router, F, Bot

from core.config import TOKEN
from keyboards.admin import admin
from fsm.states import Admin
from database.clients_database import clients

router = Router()
bot = Bot(token=TOKEN)

@router.callback_query(F.data == "send_birth_mailing")
async def send_birth_mailing_text(callback: types.CallbackQuery, state: FSMContext):
    admin.back_to_menu()
    await callback.message.answer("Введи сообщение, которое хочешь отправить всем именинникам",
                                  reply_markup=admin.builder.as_markup(resize_keyboard=True))
    await state.set_state(Admin.mailing)


@router.message(Admin.mailing)
async def get_mailing_text(message: types.Message, state: FSMContext):
    text = message.text
    admin.mailing_photo()
    await message.answer("Отправь фото, которое прикрепишь к посту",
                         reply_markup=admin.builder.as_markup(resize_keyboard=True))
    await state.set_state(Admin.mailing_photo)
    await state.update_data(text=text)


@router.message(Admin.mailing_photo)
async def get_birth_mailing_photo(message: types.Message, state: FSMContext):
    # Получаем последнее фото из сообщения
    photo = message.photo[-1]  # Берем самое высокое разрешение # Загружаем фото
    photo_file = await message.bot.download(file=photo.file_id)

    # Извлекаем текст из состояния
    data = await state.get_data()
    text = data.get("text", "")  # Получаем текст, если он есть

    admin.sending_mailing_menu()
    await message.answer_photo(photo=photo.file_id, caption=text,
                               reply_markup=admin.builder.as_markup(resize_keyboard=True))


@router.callback_query(F.data == "without_photo")
async def mailing_without_photo(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    t = data.get("text", "")  # Получаем текст, если он есть

    admin.sending_mailing_menu()
    await callback.message.answer(text=t,
                                  Фreply_markup=admin.builder.as_markup(resize_keyboard=True))


@router.callback_query(F.data == "send_post")
async def mailing_without_photo(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    t = data.get("text", "")  # Получаем текст, если он есть
    id_list = clients.get_clients_number_with_birthday()
    for id in id_list:
        await bot.send_message(chat_id=id, text=t)

    admin.back_to_menu()
    await state.clear()
    await callback.message.answer("Рассылка произведена",
                                  reply_markup=admin.builder.as_markup(resize_keyboard=True))


