from aiogram import types, Bot
from aiogram.types import FSInputFile
from core.constants import (freebet_birth,
                                freebet_reg, freebet_link_discription01, freebet_link_discription02)
from core import config
from keyboards.menu import menu

TOKEN = config.TOKEN  # Используйте токен из конфигурации
bot = Bot(token=TOKEN)
photo_04 = FSInputFile("Черный.jpg")


async def stocks(callback: types.CallbackQuery):
    menu.event()
    await callback.message.answer_photo(photo_04, "Наши акции",
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))


async def free_bet_01(callback: types.CallbackQuery):
    menu.back_to_menu_2()
    await callback.message.answer_photo(photo_04, freebet_birth,
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))


async def free_bet_02(callback: types.CallbackQuery):
    menu.back_to_menu_2()
    await callback.message.answer_photo(photo_04, freebet_reg,
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))


async def free_bet_03(callback: types.CallbackQuery):
    user_id = callback.message.chat.id
    print(callback.message.chat.id)
    print(user_id)

    try:
        # Проверка первого чата
        user_channel_status = await bot.get_chat_member(chat_id='-1002447096182', user_id=user_id)
        print(user_channel_status.status)
        if user_channel_status.status != 'member' and user_channel_status.status != 'administrator':
            menu.channel()
            await callback.message.answer_photo(photo_04, freebet_link_discription02,
                                                reply_markup=menu.builder.as_markup(resize_keyboard=True))
        else:
            menu.group()
            await callback.message.answer_photo(photo_04, freebet_link_discription01,
                                                reply_markup=menu.builder.as_markup(resize_keyboard=True))
    except Exception as e:
        await callback.message.answer(f'Произошла ошибка при проверке первого чата: {str(e)}')


async def cancel(callback: types.CallbackQuery):
    menu.event()
    await callback.message.answer_photo(photo_04, "Наши акции",
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))