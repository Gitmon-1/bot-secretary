from aiogram import Router, types
from aiogram.filters import Command
from algorithms.find_info import show
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.state import FSMContext
from convertor import save_to_json
from kb import main_menu_keyboard, add_menu_kb, under_category_menu_kb, text_menu_kb, search_menu_kb, delete_menu_kb
from handlers.handler import AddText


find_router = Router()  


@find_router(lambda msg: msg.text == "Поиск")
async def show_cmd(message: types.Message):
    pass