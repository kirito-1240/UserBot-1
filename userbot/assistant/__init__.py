from telethon import TelegramClient
from Config import Config
import sys
import time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

try:
    bot = TelegramClient(
        "UserBotAssistant",
        API_ID,
        API_HASH,
    ).start(bot_token=BOT_TOKEN)

except Exception as e:
    print(f"• Error On Create App Assistant: {e}")
    sys.exit()
