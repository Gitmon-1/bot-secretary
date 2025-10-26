from aiogram import Router, types
from aiogram.filters import Command
from algorithms.sorting_algorithm import sorting
from algorithms.delete_info import delete
from algorithms.show_info import show
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.state import FSMContext
from convertor import save_to_json
import json
import os

router = Router()


class AddText(StatesGroup):
    waiting_for_text = State()


@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Добро пожаловать!\nИспользуй /MENU чтобы добавить текст.")

@router.message(Command("Add"))
async def add_cmd(message: types.Message, state: FSMContext):
    await message.answer("Введите текст для добавления в конспект:")
    await state.set_state(AddText.waiting_for_text)

@router.message(AddText.waiting_for_text)
async def save_text(message: types.Message, state: FSMContext):
    user_text = message.text
    save_to_json(user_text)
    await message.answer(f"✅ Текст сохранён:\n{user_text}")
    await state.clear()

@router.message(Command("Show"))
async def show_cmd(message: types.Message):
    pass

@router.message(Command("Delete"))
async def delete_cmd(message: types.Message):
    await delete(f"Сортирую {message.text}")