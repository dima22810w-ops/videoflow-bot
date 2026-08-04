from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

subscribe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Канал 1",
                url="https://t.me/avatartgia"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Канал 2",
                url="https://t.me/avtoblogtgai"
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 Канал 3",
                url="https://t.me/xzrgai"
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
