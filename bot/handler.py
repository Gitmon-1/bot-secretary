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
    waiting_for_keywords = State()


@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Добро пожаловать!\nИспользуй /MENU чтобы добавить текст.")


@router.message(Command("Добавить"))
async def add_cmd(message: types.Message, state: FSMContext):
    await message.answer("✍️ Введите текст для добавления в конспект:")
    await state.set_state(AddText.waiting_for_text)


@router.message(AddText.waiting_for_text)
async def receive_text(message: types.Message, state: FSMContext):
    await state.update_data(user_text=message.text)
    await message.answer("🔑 Теперь введите ключевые слова:")
    await state.set_state(AddText.waiting_for_keywords)


@router.message(AddText.waiting_for_keywords)
async def receive_keywords(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_text = data.get("user_text")
    user_keywords = message.text

    await save_to_json({"text": user_text, "keywords": user_keywords})
    await message.answer(f"✅ Текст сохранён:\n{user_text}\n\n🔎 Ключевые слова:\n{user_keywords}")
    await state.clear()


@router.message(Command("Поиск"))
async def show_cmd(message: types.Message):
    pass


@router.message(Command("Удалить"))
async def delete_cmd(message: types.Message):
    await delete(f"Сортирую {message.text}")