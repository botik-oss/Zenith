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


admin = Admin()
