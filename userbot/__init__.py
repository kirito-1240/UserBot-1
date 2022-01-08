from telethon import TelegramClient
from telethon.sessions import StringSession
from Config import Config
import time
import sys
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

API_ID = Config.API_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION
VERSION = "1.0.6"
LOOP = None


app = TelegramClient(StringSession(str(STRING_SESSION)) , API_ID, API_HASH, loop=LOOP, app_version=VERSION, connection=ConnectionTcpAbridged, auto_reconnect=True, connection_retries=None)

START_TIME = time.time()
