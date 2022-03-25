from userbot import app , LOG_GROUP
from userbot.events import alien
from telethon import functions
from userbot.database.antispam import add_user, get_user, del_user, set_power, get_power, set_limit, get_limit

@alien(pattern="(?i)^\.santi (on|off)$")
async def set_type(event):
    await event.edit("`• Please Wait . . .`")
    pow = event.pattern_match.group(1)
    if pow.lower() == "on":
        set_power("on")
        await event.edit("**• Anti Spam Has Been Actived!**")
    else:
        set_power("off")
        await event.edit("**• Anti Spam H as Been DeActived!**")

@alien(pattern="(?i)^\.salimit (\d*)$")
async def set_lim(event):
    await event.edit("`• Please Wait . . .`")
    lim = event.pattern_match.group(1)
    set_limit(lim)
    await event.edit(f"**• Anti Spam Limit Was Set To ( {lim} )**")

@alien(incoming=True , private_only=true)
async def add_users(event):
    add_user(event.peer_id.user_id)
    if get_power() == "on" and not (await event.get_user()).bot:
        if int(get_user(event.peer_id.user_id)) == int(get_limit()):
            await event.reply("**• Your Warns Were Exceeded!**\n\n__• You Are Blocked!__")
            await app(functions.contacts.BlockRequest(id=event.peer_id.user_id))
            info = await app.get_entity(event.peer_id.user_id)
            await app.send_message(LOG_GROUP, f"**• User** [{info.first_name}](tg://user?id={info.id})\n**For Spam In Pv Has Been Blocked You Can Get And Unblock This User!**")
            del_user(event.peer_id.user_id)
        else:
            if int(get_user(event.peer_id.user_id)) == 0 or int(get_user(event.peer_id.user_id)) % 3 == 0:
                await event.reply(f"""**• Please Not Send Pms On My Pv In This Time!**\n\n**• Your Warns: ( {get_user(event.peer_id.user_id)}/{get_limit()} )**""")

@alien(pattern="(?i)^\.dwanti$" , private_only=true)
async def set_lim(event):
    await event.edit("`• Please Wait . . .`")
    id = event.peer_id.user_id
    del_user(id)
    await event.edit(f"**• Anti Spam Warns Deleted For This User!**")
