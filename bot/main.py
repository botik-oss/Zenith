from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from bot.handlers.questions import ask_question
from bot.handlers.info import stocks, free_bet_01, free_bet_02, free_bet_03
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from keyboards.menu import menu
from handlers.contacts import contacts  # Import the contacts function
from handlers.addresses import adresses
from core import config
from handlers import account

# Initialize bot and dispatcher
TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(account.router)

photo_01 = FSInputFile("Черный.jpg")


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    menu.main_menu()
    await message.answer_photo(photo_01, "Выберите опцию:",
        reply_markup=menu.builder.as_markup(resize_keyboard=True))




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

@dp.callback_query(F.data == "questions")
async def ask_your_question(callback: types.CallbackQuery):
    await ask_question(callback)

# Start polling if this script is the main one
if __name__ == "__main__":
    dp.run_polling(bot)
