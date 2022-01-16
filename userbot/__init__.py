from telethon import TelegramClient
from telethon.sessions import StringSession
from Config import Config
import sys
import time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION

try:
    app = TelegramClient(
        StringSession(str(STRING_SESSION)),
        API_ID,
        API_HASH,
    )
except Exception as e:
    print(f"• Error On Create App : {e}")
    sys.exit()


START_TIME = time.time()
