from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.state import FSMContext
from convertor import save_to_json
from kb import main_menu_keyboard, add_menu_kb, under_category_menu_kb, text_menu_kb, search_menu_kb, delete_menu_kb
from handlers.handler import AddText

add_router = Router()

@add_router.message(lambda msg: msg.text == "Добавить")
async def add_cmd(message: types.Message, state: FSMContext):
    await message.answer("✍️ Введите текст для добавления в конспект:", reply_markup=add_menu_kb)
    await state.set_state(AddText.waiting_for_text)


@add_router.message(AddText.waiting_for_text)
async def receive_text(message: types.Message, state: FSMContext):
    await state.update_data(user_text=message.text)
    await message.answer(
        "Теперь введите категорию:",
        reply_markup=add_menu_kb
    )
    await state.set_state(AddText.waiting_for_category)


@add_router.message(AddText.waiting_for_under_category)
async def receive_category(message: types.Message, state: FSMContext):
    await state.update_data(user_category=message.text)
    await message.answer(
        "Введите подкатегорию:",
        reply_markup=under_category_menu_kb
    )
    await state.set_state(AddText.waiting_for_under_category)


@add_router.message(AddText.waiting_for_under_category)
async def receive_under_category(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_text = data.get("user_text")
    user_category = data.get("user_category")
    user_under_category = message.text
    dict = {user_category: (user_under_category, user_text)}

    await save_to_json(dict)
    await message.answer(
        f"✅ Сохранено!\n"
        f"📝 Текст: {user_text}\n"
        f"📁 Категория: {user_category}\n"
        f"📂 Подкатегория: {user_under_category}",
        reply_markup=main_menu_keyboard
    )
    await state.clear()
