import argparse
import asyncio
import os

from dotenv import load_dotenv
from loguru import logger
from telethon import TelegramClient

from . import handlers

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--app_id", default=os.getenv("APP_ID", "2040"), type=int)
parser.add_argument("--app_hash", default=os.getenv("APP_HASH", "b18441a1ff607e10a989891a5462e627"))

user = parser.add_argument_group('User')
user.add_argument("--phone", default=os.getenv("PHONE"))
user.add_argument("--password", default=os.getenv("PASSOWRD"))

bot = parser.add_argument_group('Bot')
bot.add_argument("--token", default=os.getenv("BOT_TOKEN"))

args = parser.parse_args()

bot = TelegramClient("auti_lang_bot", args.app_id, args.app_hash)


async def main():
    try:
        await bot.start(
            phone=args.phone,
            password=args.password,
            bot_token=args.token,
        )
        await handlers.init(bot)
        me = await bot.get_me()
        logger.info(me.stringify())
        logger.info("Bot initialized successfully")
    except Exception as e:
        logger.error(f"Error Initializing bot: {e}")
    try:
        await bot.run_until_disconnected()
    finally:
        await bot.disconnect()

asyncio.run(main())
