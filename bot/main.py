from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from ZenithBot.bot.handlers.contacts import contacts  # Import the contacts function
from ZenithBot.bot.handlers.addresses import adresses
from ZenithBot.bot.handlers.info import stocks, free_bet_01, free_bet_02
from aiogram import F
from ZenithBot.bot.keyboards.menu import menu

# Initialize bot and dispatcher
TOKEN = '7859510119:AAEGBXuw1f52n14AI6MDX6vUFG14ol580Vc'
bot = Bot(token=TOKEN)
dp = Dispatcher()
photo_01 = FSInputFile("Черный.jpg")

# Command handler for /start

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    menu.main_menu()
    await message.answer_photo(photo_01, "Выберите опцию:",
                         reply_markup=menu.builder.as_markup(resize_keyboard=True))

@dp.callback_query(F.data == "menu")
async def return_main_menu(callback: types.CallbackQuery):
    menu.main_menu()
    await callback.message.answer_photo(photo_01, "Выберите опцию:",
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