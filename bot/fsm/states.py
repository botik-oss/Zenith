from aiogram.fsm.state import State, StatesGroup


class Account(StatesGroup):
    registration = State()
