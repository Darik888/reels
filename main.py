import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой новый помощник. Напиши что-нибудь или воспользуйся командами.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())