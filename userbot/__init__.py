from telethon import TelegramClient
from telethon.sessions import StringSession
from Config import Config
import sys
import time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
SESSION = Config.SESSION

try:
    app = TelegramClient(
        StringSession(str(SESSION)),
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
    ).start(bot_token=Config.BOT_TOKEN)

except Exception as e:
    print(f"• Error On Create App Assistant: {e}")
    sys.exit()

START_TIME = time.time()
LOG = Config.LOG_GROUP
