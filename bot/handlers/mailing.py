from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from keyboards.admin import admin
from fsm.states import Admin
from aiogram import types, Router, F

router = Router()


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
                                  reply_markup=admin.builder.as_markup(resize_keyboard=True))
