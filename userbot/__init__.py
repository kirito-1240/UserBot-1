from telethon import TelegramClient
from telethon.sessions import StringSession
from userbot.database import DB
import sys , time
from logging import getLogger

LOGS = getLogger("USER-BOT")
LOGSA = getLogger("ASSISTANT-BOT")
START_TIME = time.time()
LOG = DB.get_key("LOG_GROUP")
API_ID = DB.get_key("API_ID")
API_HASH = DB.get_key("API_HASH")
SESSION = DB.get_key("SESSION")

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
    LOGSA.error(f"• Error On Create App Assistant: {e}")
