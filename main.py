import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import aiohttp

# Настройки — вставь свои ключи
BOT_TOKEN = "8047105672:AAGjjR3N8IkixNAWiHSnxZDVe9-305GZdjc"
OPENROUTER_API_KEY = "твой_openrouter_api_ключ"
MODEL = "openai/gpt-4-turbo"  # или "mistralai/mistral-7b-instruct"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def ask_openrouter(message_text: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": message_text}],
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=json_data) as resp:
            if resp.status != 200:
                return f"Ошибка API: {resp.status}"
            data = await resp.json()
            return data["choices"][0]["message"]["content"]

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой ИИ-помощник. Спроси что угодно.")

@dp.message()
async def echo(message: types.Message):
    await message.chat.do("typing")
    try:
        response = await ask_openrouter(message.text)
        await message.answer(response)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())