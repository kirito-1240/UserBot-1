import os

class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    SESSION = os.environ.get("SESSION")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    LOG_GROUP = os.environ.get("LOG_GROUP")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API = os.environ.get("HEROKU_API")
    REDIS_URL = os.environ.get("REDIS_URL", None)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
    MongoDB_URL = os.environ.get("MongoDB_URL", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
