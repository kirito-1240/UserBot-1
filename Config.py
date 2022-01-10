import os

class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    STRING_SESSION = os.environ.get("STRING_SESSION")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API = os.environ.get("HEROKU_API")
