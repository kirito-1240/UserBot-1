from telethon import TelegramClient
from telethon.sessions import StringSession
from Config import Config
import time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION

app = TelegramClient(StringSession(str(STRING_SESSION)) , API_ID, API_HASH) 

app.send_message(Config.BOT_GROUP , "Hi✓✓")

START_TIME = time.time()
