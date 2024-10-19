from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.core.constants import questions
from bot.core.constants import channel_url, group_url


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
            callback_data="complaint_1"
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
        self.question_buttons = []  # Список для хранения кнопок вопросов def back_to_menu(self):
        self.button_11 = types.InlineKeyboardButton(
            text="оставить жалобу",
            callback_data="complaint_2"
        )
        self.button_12 = types.InlineKeyboardButton(
            text="отмена",
            callback_data="complaint_1"
        )
        self.button_13 = types.InlineKeyboardButton(
            text=list(questions)[0],
            callback_data="question_1"
        )
        self.button_14 = types.InlineKeyboardButton(
            text=list(questions)[1],
            callback_data="question_2"
        )
        self.button_15 = types.InlineKeyboardButton(
            text=list(questions)[2],
            callback_data="question_3"
        )
        self.button_16 = types.InlineKeyboardButton(
            text=list(questions)[3],
            callback_data="question_4"
        )
        self.button_17 = types.InlineKeyboardButton(
            text="подписаться",
            url=channel_url
        )
        self.button_18 = types.InlineKeyboardButton(
            text="группа с розыгрышами",
            url=group_url
        )
        self.button_19 = types.InlineKeyboardButton(
            text="отмена",
            callback_data="cancel"
        )
        self.button_20 = types.InlineKeyboardButton(
            text="{ АДМИНКА }",
            callback_data="admin"
        )

    def back_to_menu(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_7)

    # функция для меню частых вопросв
    def back_to_menu_1(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_3)
        self.builder.row(self.button_7)

    # функция для меню акций
    def back_to_menu_2(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_1)
        self.builder.row(self.button_7)

    def main_menu(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_1)
        self.builder.row(self.button_2)
        self.builder.row(self.button_3)
        self.builder.row(self.button_4)
        self.builder.row(self.button_5)
        self.builder.row(self.button_6)

    def admin_menu(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_1)
        self.builder.row(self.button_2)
        self.builder.row(self.button_3)
        self.builder.row(self.button_4)
        self.builder.row(self.button_5)
        self.builder.row(self.button_6)
        self.builder.row(self.button_20)

    def event(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_8)
        self.builder.row(self.button_9)
        self.builder.row(self.button_10)
        self.builder.row(self.button_7)

    def new_button(self, text, callback):
        new_button = types.InlineKeyboardButton(
            text=text,
            callback_data=callback)
        self.question_buttons.append(new_button)  # Добавляем новую кнопку в список

    # функция для меню акций
    def group(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_18)
        self.builder.row(self.button_19)

    def channel(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_17)
        self.builder.row(self.button_19)

    def complaine_1(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_11)
        self.builder.row(self.button_7)

    def complaine_2(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_7)

    def question(self):
        self.builder = InlineKeyboardBuilder()
        self.builder.row(self.button_13)
        self.builder.row(self.button_14)
        self.builder.row(self.button_15)
        self.builder.row(self.button_16)
        for button in self.question_buttons:  # Добавляем все кнопки из question_buttons
            self.builder.row(button)
        self.builder.row(self.button_7)  # Добавляем кнопку "главное меню"


menu = Menu()
