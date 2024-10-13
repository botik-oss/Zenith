from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from keyboards.menu import Menu
from handlers.contacts import contacts  # Import the contacts function
from handlers.addresses import adresses
from aiogram import F
from core import config

# Initialize bot and dispatcher
TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Command handler for /start
menu = Menu()
menu.main_menu()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Выберите опцию:",
                         reply_markup=menu.builder.as_markup(resize_keyboard=True))


# Add a callback handler for the contacts button
@dp.callback_query(F.data == "contacts")
async def handle_contacts(callback: types.CallbackQuery):
    await contacts(callback)


@dp.callback_query(F.data == "adresses")
async def handle_adresses(callback: types.CallbackQuery):
    await adresses(callback)


# Start polling if this script is the main one
if __name__ == "__main__":
    dp.run_polling(bot)
