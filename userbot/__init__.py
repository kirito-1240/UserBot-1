from telethon import TelegramClient
from userbot.database import SqlDB
from telethon.sessions import StringSession
from Config import Config
import sys
import time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION
BOT_TOKEN = Config.BOT_TOKEN

try:
    app = TelegramClient(
        StringSession(str(STRING_SESSION)),
        API_ID,
        API_HASH,
    ).start()
except Exception as e:
    print(f"• Error On Create App : {e}")
    sys.exit()

try:
    bot = TelegramClient(
        "UserBotAssistant",
        API_ID,
        API_HASH,
    ).start(bot_token=BOT_TOKEN)

except Exception as e:
    print(f"• Error On Create App Assistant: {e}")
    sys.exit()

START_TIME = time.time()
LOG = Config.LOG_GROUP
DB = SqlDB(Config.DATATBASE_URL)
