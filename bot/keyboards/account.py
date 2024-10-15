from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Account:
    def __init__(self):
        self.builder = InlineKeyboardBuilder()

        self.button_1 = types.InlineKeyboardButton(
            text="Главное меню",
            callback_data="start"
        )

        self.button_2 = types.InlineKeyboardButton(
            text="Персональные акции",
            callback_data="shares"
        )

    def back_to_menu(self):
        self.builder.row(
            self.button_1
        )

    def build_account(self):
        self.builder.row(self.button_2)
        self.builder.row(self.button_1)


account = Account()
