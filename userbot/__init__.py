from pyrogram import Client
from Config import Config
import sys , time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION
VERSION = "1.0.6"

try:
    app = Client(
        session = STRING_SESSION,
        api_id = API_ID,
        api_hash = API_HASH,
        app_version = VERSION
    )
except Exception as e:
    print(f"• Error On Create App : {e}")
    sys.exit()


START_TIME = time.time()
