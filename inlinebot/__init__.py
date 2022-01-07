from telethon import TelegramClient
from Config import Config
import time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN = Config.BOT_TOKEN

bot = TelegramClient('InlineBot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

START_TIME = time.time()
