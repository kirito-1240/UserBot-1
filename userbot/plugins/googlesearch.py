from userbot import app
from userbot.events import alien
from userbot.functions.tools import google_search

@alien(pattern="gsearch (.*)")
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

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Search On Google!",
        "commands": {
            "{cmdh}gsearch [query]": "To Search On Google By Given Query!",
        },
    }
})
