from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.tag$"))
async def TagMembers(event):
    st = await event.edit("`• Starting Tag Members ...`")
    list = []
    async for user in app.iter_participants(chat_id):
        if not user.bot and not user.deleted:
            if user.username:
                list.append("@" + user.username)
            else:
                list.append(f"[user.first_name](tg://user?id={user.id})")
    for user in chunks(list , 5):
        edit = await app.send_message(event.chat_id , "\n".join(user))
        await edit.edit("****__• Tag Members!**__**")
    await st.edit("**• Tag Members Completed!**")
