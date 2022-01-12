from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.tag ?(.*)?$"))
async def TagMembers(event):
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
    for user in chunks(list , 30):
        edit = await app.send_message(event.chat_id , "\n".join(user))
        await app.send_message('me' , "\n".join(user))
        await edit.edit("**__• Tag Members!**__")
    await st.edit(f"""**__• Tag Members Completed!**__""")
