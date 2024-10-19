from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from keyboards.admin import admin

router = Router()
photo_01 = FSInputFile("Черный.jpg")


@router.callback_query(F.data == "admin")
async def admin_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    admin.build_admin()
    await callback.message.answer_photo(photo_01, "Админка",
                                        reply_markup=admin.builder.as_markup(resize_keyboard=True))
