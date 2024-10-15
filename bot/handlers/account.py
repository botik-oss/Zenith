from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from database.clients_database import clients
from database.clients_telegram_database import clients_telegram
from keyboards.account import account as acc
from fsm.states import Account

router = Router()


@router.callback_query(F.data == "account")
async def log_account(callback: types.CallbackQuery, state: FSMContext):
    print('1')
    user_id = callback.message.from_user.id
    if not await clients_telegram.check_client_exist_by_id(user_id):
        await callback.message.answer("Личным кабинетом могут пользоваться только авторизованные пользователи!\n"
                                      "\nЧтобы авторизоваться введи  свой номер игрока",
                                      reply_markup=acc.builder.as_markup(resize_keyboard=True))
        await state.set_state(Account.registration)
    else:
        await callback.message.answer("Личный кабинет",
                                      reply_markup=acc.builder.as_markup(resize_keyboard=True))


@router.message(Account.registration)
async def registrate_account(message: types.Message):
    number = message.text
    if await clients.check_client_exist(number) and not (await clients_telegram.check_client_exist_by_number(number)):
        user_id = message.from_user.id
        user_username = message.from_user.username
        await clients_telegram.add_client(int(number), user_id, user_username)
    else:
        print('2')
