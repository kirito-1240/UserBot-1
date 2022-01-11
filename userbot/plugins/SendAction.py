from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.saction (\S*) (\d*)$"))
async def SendAction(event):
    edit = await event.edit("`• Please Wait ...`")
    action = event.match_pattern.group(1)
    time = int(event.match_pattern.group(2))
    try:
        async with app.action(event.chat_id , action):
            await edit.edit(f"`• Sending {action} Action For {time}s On This Chat ...`")
            await sleep(time)
            await edit.delete()
            await app.send_message(event.chat_id , "**• Send Action Completed!**")
    except ValueError:
        await edit.edit("**• Your Action Not Found!**")
