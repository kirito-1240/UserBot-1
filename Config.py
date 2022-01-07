import os

class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    STRING_SESSION = os.environ.get("STRING_SESSION")
    BOT_GROUP = os.environ.get("BOT_GROUP")
