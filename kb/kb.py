from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Add')], 
        [KeyboardButton(text='Show')],
        [KeyboardButton(text='Delete')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...'
)   