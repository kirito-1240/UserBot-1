from userbot import app , LOG
from telethon import events, functions
from userbot.database.antispam import add_user, get_user, del_user, set_power, get_power, set_limit, get_limit

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.santi (on|off)$"))
async def set_type(event):
    await event.edit("`• Please Wait . . .`")
    pow = event.pattern_match.group(1)
    if pow.lower() == "on":
        set_power("on")
        await event.edit("**• Anti Spam Has Been Actived!**")
    else:
        set_power("off")
        await event.edit("**• Anti Spam H as Been DeActived!**")

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.salimit (\d*)$"))
async def set_lim(event):
    await event.edit("`• Please Wait . . .`")
    lim = event.pattern_match.group(1)
    set_limit(lim)
    await event.edit(f"**• Anti Spam Limit Was Set To ( {lim} )!**")

@app.on(events.NewMessage(incoming=True))
async def add_users(event):
    if get_power() == "on" and not event.from_id:
        if int(get_user(event.peer_id.user_id)) == int(get_limit()):
            await event.reply("**• Your Warns Were Exceeded!**\n\n__• You Are Blocked!__")
            await app(functions.contacts.BlockRequest(id=event.peer_id.user_id))
            del_user(event.peer_id.user_id)
        else:
            add_user(event.peer_id.user_id)
            if int(get_user(event.peer_id.user_id)) == 0 or int(get_user(event.peer_id.user_id)) % 3 == 0:
                await event.reply(f"""**• Please Not Send Pms On My Pv In This Time!**\n\n**• Warns: ( {get_user(event.peer_id.user_id)}/{get_limit()} )""")
