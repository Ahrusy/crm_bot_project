import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DJANGO_API_URL = os.getenv("DJANGO_API_URL")  # Например: http://localhost:8000/api/

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Напиши /myinfo, чтобы получить информацию о себе.")

@dp.message(Command("myinfo"))
async def get_my_info(message: types.Message):
    telegram_id = message.from_user.id
    url = f"{DJANGO_API_URL}agent/{telegram_id}/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            text = (
                f"👤 Имя: {data.get('name')}\n"
                f"Роль: {data.get('role')}\n"
                f"Сделок в работе: {data.get('deals_in_progress')}\n"
                f"Выручка в этом месяце: {data.get('current_month_revenue')}"
            )
        elif response.status_code == 404:
            text = "❗Пользователь не найден в базе."
        else:
            text = "🚫 Ошибка при получении данных. Попробуйте позже."
    except requests.RequestException as e:
        logging.error(f"Ошибка запроса: {e}")
        text = "⚠️ Ошибка соединения с сервером."

    await message.reply(text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
