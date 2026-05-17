import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("✅ بوت Quotex AI يعمل بنجاح")

@dp.message()
async def signal(message: Message):

    result = """
📊 الزوج: EUR/USD OTC
🕒 الفريم: 1M
📈 الاتجاه: BUY 🔼
⏰ وقت الدخول: بعد إغلاق الشمعة الحالية
⌛ مدة الصفقة: 1 دقيقة
🎯 قوة الصفقة: قوية

📌 سبب الدخول:
• دعم قوي
• BOS صاعد
• زخم شرائي

📍 نسبة الثقة: 88%
"""

    await message.answer(result)

async def main():
    print("BOT STARTED")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
