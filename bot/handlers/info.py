from aiogram import types, Bot
from aiogram.types import FSInputFile
from core.constants import (freebet_birth,
                            freebet_reg, freebet_link_discription01, freebet_link_discription02)
from keyboards.menu import menu

TOKEN = '7749968130:AAFjs5xMiI1gBhIvn5C1qNYeEIQjYpABMPM'
bot = Bot(token=TOKEN)


async def stocks(callback: types.CallbackQuery):
    photo_04 = FSInputFile("Черный.jpg")
    menu.event()
    await callback.message.answer_photo(photo_04, "Наши акции",
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True)
                                        )


async def free_bet_01(callback: types.CallbackQuery):
    photo_04 = FSInputFile("Черный.jpg")
    menu.back_to_menu()
    await callback.message.answer_photo(photo_04, freebet_birth,
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True)
                                        )


async def free_bet_02(callback: types.CallbackQuery):
    photo_04 = FSInputFile("Черный.jpg")
    menu.back_to_menu()
    await callback.message.answer_photo(photo_04, freebet_reg,
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True)
                                        )


async def free_bet_03(callback: types.CallbackQuery):
    user_id = callback.message.from_user.id
    photo_04 = FSInputFile("Черный.jpg")
    user_channel_status = await bot.get_chat_member(chat_id='-1001954045115', user_id=user_id)
    if user_channel_status["status"] != 'left':
        await callback.message.answer(freebet_link_discription02)
    else:
        await callback.message.answer_photo(photo_04, freebet_link_discription01,
                                            reply_markup=menu.builder.as_markup(resize_keyboard=True))
