from aiogram import types, Router
from aiogram.filters import Command

from keyboards.menu import menu
from main import photo_01
from database.admins_database import admins
router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    if admins.check_admin_exist(message.from_user.id):
        menu.admin_menu()
    else:
        menu.main_menu()
    await message.answer_photo(photo_01, "Выберите опцию:",
                               reply_markup=menu.builder.as_markup(resize_keyboard=True))