import argparse
import os

from dotenv import load_dotenv
from loguru import logger
from telethon import TelegramClient

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--app_id", default=os.getenv("APP_ID", "2040"), type=int)
parser.add_argument(
    "--app_hash", default=os.getenv("APP_HASH", "b18441a1ff607e10a989891a5462e627")
)
parser.add_argument("--token", default=os.getenv("BOT_TOKEN"))

args = parser.parse_args()

client = TelegramClient("auti_lang_bot", args.app_id, args.app_hash)
bot = client.start(bot_token=args.token)


async def main():
    me = await client.get_me()
    logger.info(me.stringify())


with bot:
    bot.loop.run_until_complete(main())
