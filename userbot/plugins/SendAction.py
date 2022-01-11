from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.saction ?(\S*)? ?(\d*)?$"))
async def SendAction(event):
    edit = await event.edit("`• Please Wait ...`")
    if event.pattern_match.group(1):
        action = event.pattern_match.group(1)
    else:
        action = "typing"
    if event.pattern_match.group(2):
        time = int(event.pattern_match.group(2))
    else:
        time = 30
    try:
        async with app.action(event.chat_id , action):
            await edit.edit(f"`• Sending {action} Action For {time}s On This Chat ...`")
            await sleep(time)
            await edit.delete()
            await app.send_message(event.chat_id , f"**• Send {action} Action Completed!**")
    except ValueError:
        await edit.edit("**• Your Action Not Found!**")
