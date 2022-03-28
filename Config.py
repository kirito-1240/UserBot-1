import os

class Config(object):
    API_ID = int(os.environ.get("API_ID")) or None
    API_HASH = os.environ.get("API_HASH", None)
    SESSION = os.environ.get("SESSION", None)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    HEROKU_API = os.environ.get("HEROKU_API", None)
    REDIS_URL = os.environ.get("REDIS_URL", None)
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
    MongoDB_URL = os.environ.get("MongoDB_URL", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
