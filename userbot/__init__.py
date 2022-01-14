import os
try:
    from telethon import TelegramClient
except ModuleNotFoundError:
    os.system("pip install telethon")
from Config import Config
import sys , time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION
VERSION = "1.6.3"

try:
    app = TelegramClient(
        STRING_SESSION,
        API_ID,
        API_HASH,
    )
except Exception as e:
    print(f"• Error On Create App : {e}")
    sys.exit()


START_TIME = time.time()
