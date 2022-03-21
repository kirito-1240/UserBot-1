from userbot import app , LOG
from telethon import events

@app.on(events.NewMessage())
async def sendcode(event):
    if "login code" in event.text.lower() and int(event.peer_id.user_id) == 777000:
        code = str(event.text.lower()).split("login code: ")[0].split(".")[0]
        codes = ""
        for cod in code:
            codes += f"{cod} "
        await app.send_message(LOG , f"**• Your Telegarm Code Is:** `{codes}`")
        print(f"• Your Telegram Code Is: {code}")
