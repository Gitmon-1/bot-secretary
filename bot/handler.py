from aiogram import Router, types
from aiogram.filters import Command
from algorithms.sorting_algorithm import sorting
from algorithms.delete_info import delete
from algorithms.show_info import show
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.state import FSMContext
from convertor import save_to_json
from algorithms import sorting_algorithm as sa
import json
import os


router = Router()


class AddText(StatesGroup):
    waiting_for_text = State()
    waiting_for_under_category = State()
    waiting_for_under_category = State()


@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Добро пожаловать!\nИспользуй /MENU чтобы добавить текст.")


@router.message(Command("Add"))
async def add_cmd(message: types.Message, state: FSMContext):
    await message.answer("✍️ Введите текст для добавления в конспект:")
    await state.set_state(AddText.waiting_for_text)


@router.message(AddText.waiting_for_text)
async def receive_text(message: types.Message, state: FSMContext):
    await state.update_data(user_text=message.text)
    await message.answer("🔑 Теперь введите ключевые слова:")
    await state.set_state(AddText.waiting_for_under_category)


@router.message(AddText.waiting_for_under_category)
async def receive_keywords(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_text = data.get("user_text")
    user_category = message.text

    await message.answer(f"✅ Текст сохранён:\n{user_text}\n\n🔎 Ключевые слова:\n{user_category}")
    await state.clear()


@router.message(AddText.waiting_for_under_category)
async def receive_under_category(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_text = data.get("user_text")
    user_category = data.get("user_category")
    user_under_category = message.text
    dict = {user_category: (user_under_category, user_text)}

    await save_to_json({"text": user_text, "keywords": user_category, "under_category": user_under_category})
    await message.answer(f"✅ Текст сохранён:\n{user_text}\n\n🔎 Ключевые слова:\n{user_category}\n\n📂 Подкатегория:\n{user_under_category}")
    await state.clear()


@router.message(Command("Show"))
async def show_cmd(message: types.Message):
    pass


@router.message(Command("Delete"))
async def delete_cmd(message: types.Message):
    await delete(f"Сортирую {message.text}")