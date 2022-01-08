from telethon import TelegramClient
from telethon.sessions import StringSession
from Config import Config
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import sys , time

API_ID = Config.API_ID
API_HASH = Config.API_HASH
STRING_SESSION = Config.STRING_SESSION
VERSION = "1.0.6"

try:
    app = TelegramClient(
        session = StringSession(str(STRING_SESSION)),
        api_id = API_ID,
        api_hash = API_HASH,
        app_version = VERSION,
        loop = None,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"• Error On Create App : {e}")
    sys.exit()


START_TIME = time.time()
