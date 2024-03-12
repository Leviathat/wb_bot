from aiogram import Bot, Dispatcher
import asyncio
import logging

import bot.handlers as handlers
import bot.commands as commands
import config


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(handlers.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
