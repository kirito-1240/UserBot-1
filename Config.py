import os

API_ID = int(os.environ.get("API_ID")) or None
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
COMMAND_HANDLER = os.environ.get("COMMAND_HANDLER", ".")
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API = os.environ.get("HEROKU_API", None)
REDIS_URL = os.environ.get("REDIS_URL", None)
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", None)
GIT_TOKEN = os.environ.get("GIT_TOKEN", "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")
REPO_NAME = os.environ.get("REPO_NAME", "MxAboli/UserBot")
CURRENT_DIR = os.path.dirname(__file__)
