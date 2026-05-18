from telegram.ext import Updater, CommandHandler

TOKEN = 8928367627:AAHpiqsRIHKMAKDn4I4E0OGNNIIqXMX2f3M

def start(update, context):
    update.message.reply_text("بوت Quotex AI شغال ✅")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

print("Bot Started...")
updater.start_polling()
updater.idle()
