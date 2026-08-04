import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN
from keyboards import subscribe_keyboard

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 <b>Добро пожаловать в VideoFlow!</b>\n\n"
        "📥 Здесь ты сможешь скачивать видео.\n\n"
        "❗ Для начала подпишись на наши каналы и нажми «Проверить подписку».",
        reply_markup=subscribe_keyboard
    )


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
