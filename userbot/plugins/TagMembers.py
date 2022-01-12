from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.tag ?(.*)?$"))
async def TagMembers(event):
    st = await event.edit("`• Starting Tag Members ...`")
    start = time.time()
    if event.pattern_match.group(1):
        chat_id = await app.get_entity(event.pattern_match.group(1)).id
    else:    
        chat_id = event.chat_id
    list = []
    async for user in app.iter_participants(chat_id):
        if user.username:
            list.append("@" + user.username)
    for user in chunks(list , 50):
        edit = await app.send_message(event.chat_id , "\n".join(user))
        await edit.edit("**__• Tag Members!**__")
    end = time.time()
    time = convert_time(end - start)
    await st.edit(f"""**__• Tag Members Completed! \n • Time:**__ ( `{time}` )""")
