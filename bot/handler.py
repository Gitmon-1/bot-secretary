from aiogram import Router, types
from aiogram.filters import Command
from algorithms.sorting_algorithm import sorting
from algorithms.delete_info import delete
from algorithms.show_info import show

router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Добро пожаловать!")


@router.message(Command("Add"))
async def add_cmd(message: types.Message):
    await sorting(f"Сортирую {message.text}")

@router.message(Command("Show"))
async def show_cmd(message: types.Message):
    pass

@router.message(Command("Delete"))
async def delete_cmd(message: types.Message):
    await delete(f"Сортирую {message.text}")