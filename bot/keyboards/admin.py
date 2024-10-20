from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Admin:
    def __init__(self) -> None:
        self.builder = InlineKeyboardBuilder()

        self.button_1 = types.InlineKeyboardButton(
            text="Главное меню",
            callback_data="menu"
        )

        self.button_2 = types.InlineKeyboardButton(
            text="Обновить базу",
            callback_data="database_update"
        )

        self.button_3 = types.InlineKeyboardButton(
            text="Рассылки",
            callback_data="mailing"
        )

        self.button_4 = types.InlineKeyboardButton(
            text="рассылка по именинникам",
            callback_data="birth_mailing"
        )

        self.button_5 = types.InlineKeyboardButton(
            text="рассылка всем",
            callback_data="all_mailing"
        )

        self.button_6 = types.InlineKeyboardButton(
            text="рассылка по номеру игрока",
            callback_data="number_mailing"
        )

        self.button_7 = types.InlineKeyboardButton(
            text="отмена",
            callback_data="admin"
        )
    def build_admin(self) -> None:
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_2)
        self.builder.row(self.button_3)
        self.builder.row(self.button_1)

    def back_to_menu(self) -> None:
        self.builder = InlineKeyboardBuilder()
        self.builder.row(
            self.button_1
        )

    def mailing(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_4)
        self.builder.row(self.button_5)
        self.builder.row(self.button_6)
        self.builder.row(self.button_7)

account = Admin()

admin = Admin()
