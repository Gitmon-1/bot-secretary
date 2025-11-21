from aiogram import Router, types
from aiogram.filters import Command
from algorithms.delete_info import delete
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.state import FSMContext
from kb import main_menu_keyboard, add_menu_kb, under_category_menu_kb, text_menu_kb, search_menu_kb, delete_menu_kb
from handlers.handler import AddText


delete_router = Router()


@delete_router(lambda msg: msg.text == "Удалить")
async def delete_cmd(message: types.Message, state: FSMContext):
      await message.answer("Выберите, что вы хотите удлаить", reply_markup=delete_menu_kb)
      

@delete_router(lambda msg: msg.text == "Удалить по категории")
async def delete_by_category(message: types.Message, state: FSMContext):
        await message.answer("Введите категорию для удаления", reply_markup=delete_menu_kb)
        await state.set_state(AddText.waiting_for_category)


@delete_router(AddText.waiting_for_category)
async def receive_delete_category(message: types.Message, state: FSMContext):
        user_category = message.text
        await delete(user_category)
        await message.answer(f"Категория {user_category} удалена", reply_markup=main_menu_keyboard)
        await state.clear()


@delete_router(lambda msg: msg.text == "Удалить по подкатегории")
async def delete_by_under_category(message: types.Message, state: FSMContext):
        await message.answer("Введите подкатегорию для удаления", reply_markup=delete_menu_kb)
        await state.set_state(AddText.waiting_for_under_category)


@delete_router(AddText.waiting_for_under_category)
async def receive_delete_under_category(message: types.Message, state: FSMContext):
        user_under_category = message.text
        await delete(user_under_category)
        await message.answer(f"Подкатегория {user_under_category} удалена", reply_markup=main_menu_keyboard)
        await state.clear()


@delete_router(lambda msg: msg.text == "Удалить текст")
async def delete_by_under_category(message: types.Message, state: FSMContext):
        await message.answer("Введите текст для удаления", reply_markup=delete_menu_kb) #TODO
        await state.set_state(AddText.waiting_for_text)


@delete_router(AddText.waiting_for_text)
async def receive_delete_text(message: types.Message, state: FSMContext):
        user_text = message.text
        await delete(user_text)
        await message.answer(f"Текст {user_text} удалена", reply_markup=main_menu_keyboard)
        await state.clear()


