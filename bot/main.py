from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from bot.handlers.contacts import contacts  # Import the contacts function
from bot.handlers.addresses import adresses
from bot.handlers.fsm import *
from bot.handlers.info import stocks, free_bet_01, free_bet_02
from aiogram import F
from bot.keyboards.menu import menu
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command, StateFilter
from aiogram import Router
from aiogram.fsm.context import FSMContext
from bot.core.constants import complaints
from bot.handlers.complaints import accept_to_complaint, make_complaint, send_complaint
# Initialize bot and dispatcher
TOKEN = '7536990395:AAFpT5VXsx0VuBuqoG5ha7h5pzeBQCIG1SM'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
photo_01 = FSInputFile("Черный.jpg")
router = Router()
dp.include_router(router)

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
    dp.run_polling(bot)