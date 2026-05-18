}
import os
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("✅ بوت Quotex AI يعمل بنجاح")

@dp.message_handler()
async def signal(message: types.Message):

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

if name == "main":
    executor.start_polling(dp, skip_updates=True
