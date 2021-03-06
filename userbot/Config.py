import os
import base64

API_ID = int(os.environ.get("API_ID")) or None
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
COMMAND_HANDLER = os.environ.get("COMMAND_HANDLER", ".")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API = os.environ.get("HEROKU_API", None)
REDIS_URL = os.environ.get("REDIS_URL", None)
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
GIT_TOKEN = base64.b64decode("Z2hwX1pWZklTS1dGT2YzelZQcThFYkxRVldtdjhmOU1BRzJzaEJxMg==").decode('utf-8')
