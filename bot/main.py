from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from keyboards.menu import Menu
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

# Command handler for /start
menu = Menu()
menu.main_menu()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Выберите опцию:",
                         reply_markup=menu.builder.as_markup(resize_keyboard=True))


@dp.callback_query(F.data == "menu")
async def return_main_menu(callback: types.CallbackQuery):
        await callback.message.answer(text="Выберите опцию:",
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
