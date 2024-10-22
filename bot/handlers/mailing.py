from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F, Bot

from core.config import TOKEN
from keyboards.admin import admin
from fsm.states import Admin
from database.clients_database import clients

router = Router()
bot = Bot(token=TOKEN)


@router.callback_query(F.data == "mailing")
async def mailing_menu(callback: types.CallbackQuery) -> None:
    admin.mailing()
    await callback.message.answer("виды рассылок",
                                  reply_markup=admin.builder.as_markup(resize_keyboard=True))


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
    await state.update_data(photo=photo.file_id)
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
    await callback.message.answer(t,
                                  reply_markup=admin.builder.as_markup(resize_keyboard=True))


@router.callback_query(F.data == "send_post")
async def mailing_without_photo(callback: types.CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        photo = data.get("photo", "")
        t = data.get("text", "")  # Получаем текст, если он есть
        id_list = await clients.get_clients_number_with_birthday()
        if photo:
            for id in id_list:
                await bot.send_photo(photo=photo, chat_id=id, caption=t)
        else:
            for id in id_list:
                await bot.send_message(chat_id=id, text=t)
        admin.back_to_menu()
        await state.clear()
        await callback.message.answer(
            text=f"Рассылка произведена для {len(id_list)} пользователей",
            reply_markup=admin.builder.as_markup(resize_keyboard=True)
        )
    except Exception:
        admin.back_to_menu()
        await state.clear()
        await callback.message.answer(
            text="Произошла ошибка при рассылке (скорее всего некорректный ввод текста)",
            reply_markup=admin.builder.as_markup(resize_keyboard=True)
        )


