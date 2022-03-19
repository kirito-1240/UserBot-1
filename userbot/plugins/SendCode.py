from . import *

@app.on(events.NewMessage())
async def Code(event):
    if "code" in event.text:
        print(event.text)
