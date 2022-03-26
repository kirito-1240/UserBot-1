from userbot import app
from userbot.events import alien
from userbot.functions.tools import google_search

@alien(pattern="(?i)^.gsearch (.*)$")
async def googlesearch(event):
    await event.edit("`• Please Wait . . .`")
    query = str(event.pattern_match.group(1))
    result = f"**• Google Search For Query:** ( `{query}` )\n\n"
    co = 0
    for x in await google_search(query):
        if x["title"]:
            co += 1
            result += f'**{co} -** [{x["title"]}]({x["link"]})\n\n'
    await event.edit(result)


from userbot.database import CMDS_HELP
plugin = ((__name__).split(".")[-1])
CMDS_HELP.update(
    {
        plugin:{
            "info": "To Search From Google!",
            "cmds": {".gsearch": "To Search From Google By Query!"},
            "exm": [".gsearch [query]"],
       }
    }
