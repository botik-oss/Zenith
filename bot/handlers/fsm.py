from aiogram.fsm.state import State, StatesGroup

class Complaint_menu(StatesGroup):
    action = State()
    complaint = State()
