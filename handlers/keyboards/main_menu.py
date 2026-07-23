from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def menu():

    keyboard = [
        [
            InlineKeyboardButton(
                "📱 Order",
                callback_data="order"
            )
        ],
        [
            InlineKeyboardButton(
                "💳 Pembayaran",
                callback_data="payment"
            )
        ]
    ]

    return InlineKeyboardMarkup(keyboard)
