from . import app
from userbot.utils import setup_bot

app.loop.run_until_complete(setup_bot())

try:
    app.run_until_disconnected()
except ConnectionError:
    pass
