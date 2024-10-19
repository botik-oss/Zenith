from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from handlers.complaints import accept_to_complaint, make_complaint, send_complaint
from handlers.fsm import Complaint_menu
from handlers.questions import (ask_question,
                                    ask_question_1, ask_question_2, ask_question_3, ask_question_4)
from handlers.info import stocks, free_bet_01, free_bet_02, free_bet_03, cancel
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from keyboards.menu import menu
from handlers.contacts import contacts
from handlers.addresses import adresses
from core import config
from handlers import account

# Initialize bot and dispatcher
TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
photo_01 = FSInputFile("Черный.jpg")
router = Router()
dp.include_router(account.router)
dp.include_router(router=router)


@dp.callback_query(F.data == "menu")
async def return_main_menu(callback: types.CallbackQuery) -> None:
    menu.main_menu()
    await callback.message.answer_photo(photo_01, "Выберите опцию:",
                                        reply_markup=menu.builder.as_markup(resize_keyboard=True))


# Add a callback handler for the contacts button
@dp.callback_query(F.data == "contacts")
async def handle_contacts(callback: types.CallbackQuery) -> None:
    await contacts(callback)


@dp.callback_query(F.data == "adresses")
async def handle_adresses(callback: types.CallbackQuery) -> None:
    await adresses(callback)


@dp.callback_query(F.data == "stocks")
async def stocks_menu(callback: types.CallbackQuery) -> None:
    await stocks(callback)


@dp.callback_query(F.data == "freebet_birth")
async def stocks_menu(callback: types.CallbackQuery) -> None:
    await free_bet_01(callback)


@dp.callback_query(F.data == "freebet_reg")
async def stocks_menu(callback: types.CallbackQuery) -> None:
    await free_bet_02(callback)


@dp.callback_query(F.data == "group")
async def stocks_menu(callback: types.CallbackQuery):
    await free_bet_03(callback)

@dp.callback_query(F.data == "cancel")
async def cancel_menu(callback: types.CallbackQuery):
    await cancel(callback)

@dp.callback_query(F.data == "questions")
async def ask_your_question(callback: types.CallbackQuery):
    await ask_question(callback)


@dp.callback_query(F.data == "question_1")
async def ask_your_question_1(callback: types.CallbackQuery):
    await ask_question_1(callback)


@dp.callback_query(F.data == "question_2")
async def ask_your_question_2(callback: types.CallbackQuery):
    await ask_question_2(callback)


@dp.callback_query(F.data == "question_3")
async def ask_your_question_3(callback: types.CallbackQuery):
    await ask_question_3(callback)


@dp.callback_query(F.data == "question_4")
async def ask_your_question_4(callback: types.CallbackQuery):
    await ask_question_4(callback)


@router.callback_query(F.data == "complaint_1")
async def complain_menu(callback: types.CallbackQuery, state: FSMContext):
    await accept_to_complaint(callback, state)


@router.callback_query(Complaint_menu.action)
async def complaint_menu_1(callback: types.CallbackQuery, state=FSMContext):
    await accept_to_complaint(callback, state)


@router.callback_query(Complaint_menu.complaint)
async def complaint_menu_2(callback: types.CallbackQuery, state=FSMContext):
    await make_complaint(callback, state)


@router.message(Complaint_menu.complaint)
async def send_complaint_to_admin(message: types.Message, state=FSMContext):
    await send_complaint(1041359456, message, state)


# Start polling if this script is the main one
if __name__ == "__main__":
    dp.run_polling(bot,
                   allowed_updates=["message", "inline_query", "chat_member", "callback", "callback_query"])
