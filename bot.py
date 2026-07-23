config.py
from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN
from handlers.start import start


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))


print("Bot Kedaiii Ona aktif")

app.run_polling()
