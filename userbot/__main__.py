from . import app
from userbot.utils import setup_bot

app.start()
app.run_until_disconnected(setup_bot())
