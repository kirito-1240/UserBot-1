from userbot import app
from userbot.events import alien
from userbot.database import DB
import Config, heroku3

Heroku = heroku3.from_key(Config.HEROKU_API)
APP = Heroku.apps()[Config.HEROKU_APP_NAME]

@alien(pattern="setv (.*) \| (.*)")
async def set_var(event):
    await event.edit("`• Please Wait . . .`")
    key = str(event.pattern_match.group(1))
    value = event.pattern_match.group(2)
    CONFIG = APP.config()
    if key in CONFIG:
        CONFIG[key] = value
        await event.edit(f"**• Updated Var In Heroku:**\n\n**• Key:** ( `{key}` )\n**• Value:** ( `{value}` )")
    else:
        CONFIG[key] = value
        await event.edit(f"**• Set New Var In Heroku:**\n\n**• Key:** ( `{key}` )\n**• Value:** ( `{value}` )")

@alien(pattern="delv (.*)")
async def set_var(event):
    await event.edit("`• Please Wait . . .`")
    key = str(event.pattern_match.group(1))
    CONFIG = APP.config()
    if key in CONFIG:
        await event.edit(f"**• Deleted Var From Heroku:**\n\n**• Key:** ( `{key}` )\n**• Value:** ( `{CONFIG[key]}` )")
        del CONFIG[key]
    else:
        await event.edit(f"**• This Var Is Not In Heroku!**")
