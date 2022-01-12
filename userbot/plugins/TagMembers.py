from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.tag ?(.*)?$"))
async def TagMembers(event):
    try:
        st = await event.edit("`• Starting Tag Members ...`")
        if event.pattern_match.group(1):
            chat_id = await app.get_entity(event.pattern_match.group(1))
            chat_id = chat_id.id
        else:    
            chat_id = event.chat_id
        list = []
        async for user in app.iter_participants(chat_id):
            if user.username:
                list.append("@" + user.username)
        for user in chunks(list , 5):
            edit = await app.send_message(event.chat_id , "\n".join(user))
            await edit.edit("****__• Tag Members!**__**")
        await st.edit("**• Tag Members Completed!**")
    except ValueError:
        await event.edit("**• Your Chat ID Invalid!**")
