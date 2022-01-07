from telethon import TelegramClient
from telethon.sessions import StringSession
from .Config import Config
import time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION
BOT_TOKEN = Config.BOT_TOKEN

app = TelegramClient(StringSession(str(STRING_SESSION)) , API_ID, API_HASH) 

bot = TelegramClient('InlineBot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

START_TIME = time.time()
