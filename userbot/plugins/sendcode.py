from userbot import app , LOG_GROUP
from telethon import events

@alien(incoming=True , outgoing=False)
async def sendcode(event):
    if "login code" in event.text.lower() and int(event.peer_id.user_id) == 777000:
        code = str(event.text.lower()).split("code: ")[1].split(".")[0]
        codes = ""
        for cod in code:
            codes += f"{cod} "
        await app.send_message(LOG_GROUP , f"**• Your Telegarm Code Is:** `{codes}`")
        print(f"• Your Telegram Code Is: {code}")
