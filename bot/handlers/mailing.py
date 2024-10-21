from aiogram.types import FSInputFile
from bot.keyboards.admin import account
from aiogram import types


async def mailing(callback: types.CallbackQuery):
    account.mailing()
    await callback.message.answer("виды рассылок",
                                        reply_markup=account.builder.as_markup(resize_keyboard=True))


async def send_birth_mailing(callback: types.CallbackQuery):
    account.back_to_menu()
    await callback.message.answer( "введи сообщение, которое хочешь отправить всем именинникам",
                                        reply_markup=account.builder.as_markup(resize_keyboard=True))
