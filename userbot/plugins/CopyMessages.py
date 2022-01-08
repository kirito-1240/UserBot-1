from userbot import app
from telethon import events

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.copy$"))
async def CopyMessages(event):
    reply = await event.get_reply_message()
    if not event.reply_to == None:
        if reply.fwd_from:
            await reply.forward_to(event.chat_id)    
        elif reply.media and reply.text:
            await event.reply(reply.text , file=reply.media)    
        elif reply.media:
            await  event.reply(file=reply.media)    
        else:
            await event.reply(reply.text)
        
    else:
        await event.reply("**• Please Reply To Message For Copy!**")
