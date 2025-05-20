import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

BOT_TOKEN = "7734586572:AAHUMZPV8bDT7ew65SU7xymlm6I_ykgHXsM"  # Токен в кавычках!

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой новый помощник. Напиши что-нибудь или воспользуйся командами.")

async def main():
    await dp.start_polling(bot)

if name == "__main__":
    asyncio.run(main())
