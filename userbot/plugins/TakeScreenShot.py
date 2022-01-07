from userbot import app
from telethon import events
import requests , os
        
@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.scr (.*)$"))
async def TakeScreenShot(event):
    site = str(event.text[4:])
    edit = await event.edit("`Please Wait ...`")
    response = requests.get("https://render-tron.appspot.com/screenshot/" + site, stream=True)
    with open("scr.png" , 'wb') as file:
        for chunk in response:
            file.write(chunk)
    await app.send_file(event.chat_id , "scr.png")
    os.remove("scr.png")
