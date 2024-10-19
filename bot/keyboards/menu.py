from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Menu:
    def __init__(self):
        self.builder = InlineKeyboardBuilder()
        self.button_1 = types.InlineKeyboardButton(
            text="Акции",
            callback_data="stocks"
        )
        self.button_2 = types.InlineKeyboardButton(
            text="Адреса",
            callback_data="adresses"
        )
        self.button_3 = types.InlineKeyboardButton(
            text="Частые вопросы",
            callback_data="questions"
        )
        self.button_4 = types.InlineKeyboardButton(
            text="Контакты",
            callback_data="contacts"
        )
        self.button_5 = types.InlineKeyboardButton(
            text="Жалобы",
            callback_data="complaints"
        )
        self.button_6 = types.InlineKeyboardButton(
            text="Личный кабинет",
            callback_data="account"
        )
        self.button_7 = types.InlineKeyboardButton(
            text="главное меню",
            callback_data="menu"
        )
        self.button_8 = types.InlineKeyboardButton(
            text="фрибет за регистрацию",
            callback_data="freebet_reg"
        )
        self.button_9 = types.InlineKeyboardButton(
            text="фрибет в день рождения",
            callback_data="freebet_birth"
        )
        self.button_10 = types.InlineKeyboardButton(
            text="группа с розыгрышами",
            callback_data="group"
        )


    def back_to_menu(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(
            self.button_7
        )

    def main_menu(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_1)
        self.builder.row(self.button_2)
        self.builder.row(self.button_3)
        self.builder.row(self.button_4)
        self.builder.row(self.button_5)
        self.builder.row(self.button_6)

    # return self.builder

    def event(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_8)
        self.builder.row(self.button_9)
        self.builder.row(self.button_10)
        self.builder.row(self.button_7)


menu = Menu()
