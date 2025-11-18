from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить')], 
        [KeyboardButton(text='Поиск')],
        [KeyboardButton(text='Удалить')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...'
)   

# Добавить
#   текст (заметка)
#   категория
#       подкатегория
#           текст (заметка)

# текст, категория
add_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Текст')], 
        [KeyboardButton(text='Категория')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...'
)

# подкатегория
under_category_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Подкатегория')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...'
)
# текст
text_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Текст')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...'
)

# Поиск
#   по категорри
#   по подкатегории

# Удалить
#   категорию
#   подкатегорию
#   текст (заметка)