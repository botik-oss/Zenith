from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import FSInputFile
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from handlers.questions import (ask_question,
                                ask_question_1, ask_question_2, ask_question_3, ask_question_4)
from handlers.info import stocks, free_bet_01, free_bet_02, free_bet_03, cancel
from handlers.contacts import contacts
from handlers.addresses import adresses
from core import config
from handlers import account, complaints
from handlers.start import router as start_router

# Initialize bot and dispatcher
TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(start_router)
dp.include_router(complaints.router)
dp.include_router(account.router)
dp.include_router(router=router)
photo_01 = FSInputFile("static/main_menu.png")


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

# Start polling if this script is the main one
if __name__ == "__main__":
    dp.run_polling(bot,
                   allowed_updates=["message", "inline_query", "chat_member", "callback", "callback_query"])
