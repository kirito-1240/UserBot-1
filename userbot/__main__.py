from . import app
from userbot.utils import setup_bot

app.start()
app.loop.run_until_complete(setup_bot())
