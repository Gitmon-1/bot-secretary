import asyncio
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from token import TOKEN
from handler import router

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)
    dp.include_router(router)

if __name__ == "__main__":
    asyncio.run(main())