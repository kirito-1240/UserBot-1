import sys
from Config import Config
from userbot.utils import setup_bot
from userbot.session import app

async def startup_process():
    setup_bot()
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
    print("• Your Userbot Is Officially Working!!!")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")


app.loop.run_until_complete(startup_process())


if len(sys.argv) not in (1, 3, 4):
    app.disconnect()
else:
    try:
        app.run_until_disconnected()
    except ConnectionError:
        pass
