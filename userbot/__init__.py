from telethon import TelegramClient
from telethon.sessions import StringSession
from Config import Config
import sys , time
import logging

logging.basicConfig(
    format="[%(asctime)s] : %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

LOGS = logging.getLogger("BOT")
START_TIME = time.time()
LOG_GROUP = Config.LOG_GROUP
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
    LOGS.info(f"• Error On Create App : {e}")

try:
    bot = TelegramClient(
        "UserBotAssistant",
        API_ID,
        API_HASH,
    ).start(bot_token=Config.BOT_TOKEN)

except Exception as e:
    LOGSA.info(f"• Error On Create App Assistant: {e}")
