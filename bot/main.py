from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

from aiogram.fsm.storage.memory import MemoryStorage

from handlers.info import stocks, free_bet_01, free_bet_02
from keyboards.menu import menu
from handlers.contacts import contacts  # Import the contacts function
from handlers.addresses import adresses
from aiogram import F
from core import config
from handlers import account

# Initialize bot and dispatcher
TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(account.router)

photo_01 = FSInputFile("Черный.jpg")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    menu.main_menu()
    await message.answer_photo(photo_01, "Выберите опцию:",
                               reply_markup=menu.builder.as_markup(resize_keyboard=True))


@dp.callback_query(F.data == "menu")
async def return_main_menu(callback: types.CallbackQuery):
    menu.main_menu()
    await callback.message.answer(text="Выберите опцию:",
                                  reply_markup=menu.builder.as_markup(resize_keyboard=True))


# Add a callback handler for the contacts button
@dp.callback_query(F.data == "contacts")
async def handle_contacts(callback: types.CallbackQuery):
    await contacts(callback)


@dp.callback_query(F.data == "adresses")
async def handle_adresses(callback: types.CallbackQuery):
    await adresses(callback)


@dp.callback_query(F.data == "stocks")
async def stocks_menu(callback: types.CallbackQuery):
    await stocks(callback)


@dp.callback_query(F.data == "freebet_birth")
async def stocks_menu(callback: types.CallbackQuery):
    await free_bet_01(callback)


@dp.callback_query(F.data == "freebet_reg")
async def stocks_menu(callback: types.CallbackQuery):
    await free_bet_02(callback)


# Start polling if this script is the main one
if __name__ == "__main__":
    dp.run_polling(bot)
