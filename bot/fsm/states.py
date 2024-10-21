from aiogram.fsm.state import State, StatesGroup


class Account(StatesGroup):
    registration = State()


class Admin(StatesGroup):
    updating_database = State()
    successful_update = State()


class Complaint_menu(StatesGroup):
    complaint = State()
