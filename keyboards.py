from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

subscribe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Канал 1",
                url="https://t.me/avat"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ Проверить подписку",
                callback_data="check_sub"
            )
        ]
    ]
)
