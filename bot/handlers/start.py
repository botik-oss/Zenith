from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram import F

from keyboards.menu import menu
from database.admins_database import admins

router = Router()
photo_01 = FSInputFile("Черный.jpg")


@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    if await admins.check_admin_exist(message.from_user.id):
        menu.admin_menu()
    else:
        menu.main_menu()
    await message.answer_photo(photo_01, "Выберите опцию:",
                               reply_markup=menu.builder.as_markup(resize_keyboard=True))


@router.callback_query(F.data == "menu")
async def return_main_menu(callback: types.CallbackQuery) -> None:
    if await admins.check_admin_exist(callback.from_user.id):
        menu.admin_menu()
    else:
        menu.main_menu()
    await callback.message.answer_photo(photo_01, "Выберите опцию:",
                                reply_markup=menu.builder.as_markup(resize_keyboard=True))
