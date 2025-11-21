from add import add_router
from find import find_router
from delete import delete_router
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.state import FSMContext
from convertor import save_to_json


router = Router()


routers = [
    add_router,
    find_router,
    delete_router,
    router
]


class AddText(StatesGroup):
    waiting_for_text = State()
    waiting_for_category = State()
    waiting_for_under_category = State()


@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Добро пожаловать!\nИспользуй /MENU чтобы добавить текст.", reply_markup=main_menu_keyboard)




