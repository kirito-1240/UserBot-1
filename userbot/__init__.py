from telethon import TelegramClient
from telethon.sessions import StringSession
from Config import Config
from userbot.database import DB
import sys , time
from userbot.core.logger import logging

LOGS = logging.getLogger("Alien-UserBot")
START_TIME = time.time()
LOG_GROUP = DB.get_key("LOG_GROUP")
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
    LOGS.error(f"• Error On Create App : {e}")

try:
    bot = TelegramClient(
        "UserBotAssistant",
        API_ID,
        API_HASH,
    ).start(bot_token=Config.BOT_TOKEN)

except Exception as e:
    LOGS.error(f"• Error On Create App Assistant: {e}")
