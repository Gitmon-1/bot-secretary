import asyncio
from aiogram import Bot, Dispatcher, types
from token import TOKEN
from handlers.handler import routers

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    for r in routers:
        dp.include_router(r)

    await dp.start_polling(bot)

    
if __name__ == "__main__":
    asyncio.run(main())