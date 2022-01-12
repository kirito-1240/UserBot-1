from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.tagads$"))
async def TagAdmins(event):
    st = await event.edit("`• Starting Tag Admins ...`")
    list = []
    async for user in app.iter_participants(event.chat_id , filter=ChannelParticipantsAdmins):
        if not user.bot and not user.deleted:
            if user.username:
                list.append("@" + user.username)
            else:
                list.append(f"[user.first_name](tg://user?id={user.id})")
    for user in chunks(list , 5):
        edit = await app.send_message(event.chat_id , "\n".join(user))
        await edit.edit("****__• Tag Admins!**__**")
    await st.edit("**• Tag Admins Completed!**")
