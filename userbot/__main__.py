from . import app
from userbot.utils import setup_bot

await setup_bot()

app.start()
app.run_until_disconnected()
