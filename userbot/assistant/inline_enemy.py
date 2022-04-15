from userbot.events import alien_inline, alien_callback
from telethon import Button
from userbot.database import DB
import re

@alien_callback("^enemyclose$", owner=True)
async def enemyclose(event):
    await event.edit("**• Enemy Panel Successfuly Closed!**")

@alien_inline(re.compile("setenemy_(.*)"), owner=True)
async def setenemy(event):
    userid = event.pattern_match.group(1).decode('utf-8')
    buttons = [
        [Button.inline("• All •", data=f"setenemy_{userid}_all"), Button.inline("• Pv •", data=f"setenemy_{userid}_pv"), Button.inline("• Gps •", data=f"setenemy_{userid}_gps"), Button.inline("• Here •", data=f"setenemy_{userid}_here")],
        [Button.inline("❌ Close ❌", data="enemyclose")],
    ]
    result = event.builder.article(
        title="Alien Enemy Menu!",
        text="**• Enemy Panel:**\n\n**• Please Chose Location To Set Enemy!**",
        buttons=buttons,
    )
    await event.answer([result])

@alien_callback(re.compile("setenemy_(.*)_(.*)"), owner=True)
async def calc_callback(event):
    userid = int((event.pattern_match.group(1)).decode('utf-8'))
    loc = str((event.pattern_match.group(1)).decode('utf-8'))
    await event.edit(f"**• User Added To Enemy List: {userid} - {loc}**")
