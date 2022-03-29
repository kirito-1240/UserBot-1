from telethon import TelegramClient
from telethon.sessions import StringSession
from userbot.core.logger import LOGS
import Config
import time

START_TIME = time.time()

try:
    app = TelegramClient(
        StringSession(str(Config.SESSION)),
        Config.API_ID,
        Config.API_HASH,
        device_model="Alien Userbot",
    ).start()
except Exception as e:
    LOGS.error(f"• Error On Create App : {e}")

try:
    bot = TelegramClient(
        "UserBotAssistant",
        Config.API_ID,
        Config.API_HASH,
    ).start(bot_token=Config.BOT_TOKEN)

except Exception as e:
    LOGS.error(f"• Error On Create App Assistant: {e}")
