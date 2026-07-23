from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🌸✨ KEDAIII ONA ✨🌸

Selamat datang di bot resmi Kedaiii Ona 💗

Layanan:
📱 Nokos
🎨 Editing
📲 Aplikasi Premium
🎮 Topup MLBB
💎 Jasa Digital

Ketik /menu untuk melihat layanan.
"""
)
