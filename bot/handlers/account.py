from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from database.clients_database import clients
from database.clients_telegram_database import clients_telegram
from keyboards.account import account as acc
from fsm.states import Account

router = Router()


@router.callback_query(F.data == "account")
async def log_account(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id
    if not await clients_telegram.check_client_exist_by_id(user_id):
        acc.back_to_menu()
        await callback.message.answer("Личным кабинетом могут пользоваться только авторизованные пользователи!\n"
                                      "\nЧтобы авторизоваться введи  свой номер игрока",
                                      reply_markup=acc.builder.as_markup(resize_keyboard=True))
        await state.set_state(Account.registration)
    else:
        acc.build_account()
        await callback.message.answer("Личный кабинет",
                                      reply_markup=acc.builder.as_markup(resize_keyboard=True))


@router.message(Account.registration)
async def registrate_account(message: types.Message, state: FSMContext) -> None:
    number = message.text
    acc.back_to_menu()
    await state.clear()
    if await clients.check_client_exist(number) and not (await clients_telegram.check_client_exist_by_number(number)):
        user_id = message.from_userttttid
        user_username = message.from_user.username
        await clients_telegram.add_client(int(number), user_id, user_username)
        await message.answer("Вы успешно зарегестрированы",
                             reply_markup=acc.builder.as_markup(resize_keyboard=True))
    elif await clients_telegram.check_client_exist_by_number(int(number)):
        await message.answer("Этот номер уже занят. Уточни у кассира",
                             reply_markup=acc.builder.as_markup(resize_keyboard=True))
    else:
        await message.answer("Такого номера игрока нет в базе данных. Уточни у кассира",
                             reply_markup=acc.builder.as_markup(resize_keyboard=True))
