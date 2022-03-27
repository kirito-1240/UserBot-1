import os

class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    SESSION = os.environ.get("SESSION")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    LOG_GROUP = os.environ.get("LOG_GROUP")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API = os.environ.get("HEROKU_API")
    RMBG_API_KEY = os.environ.get("RMBG_API_KEY")
    OCR_API_KEY = os.environ.get("OCR_API_KEY")
    REDIS_URL = os.environ.get("REDIS_URL")
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
    REDIS_PORT = os.environ.get("REDIS_PORT")
    MongoDB_URL = os.environ.get("MongoDB_URL")
