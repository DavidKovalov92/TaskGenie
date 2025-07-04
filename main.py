from aiogram import Bot, Dispatcher
import asyncio
import os
import logging


logger = logging.getLogger(__name__)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    logger.info("Bot started")

    bot: Bot = Bot(token=os.getenv("TOKEN"))
    dp: Dispatcher = Dispatcher()

    await dp.start_polling(bot)


if __name__ == "__main__":
    try: 
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
