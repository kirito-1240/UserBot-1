from userbot.utils import convert_time, convert_bytes
from from userbot.functions.tools import random_headers
import time
import random
import math
import json
import requests

async def progress(current, total, event, start, type, filename):
    if type == "d":
        act = "• Downloading . . ."
    elif type == "u":
        act = "• Uploading . . ."
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elaptime = round(diff) * 1000
        tcom = round((total - current) / speed) * 1000
        eta = convert_time(elaptime + tcom)
        com = "".join(["●" for i in range(math.floor(percentage / 5))])
        percent = round(percentage, 2)
        frem = convert_bytes(current)
        ftotal = convert_bytes(total)
        text = "`{}`\n\n**• File Name:** ( `{}` )\n\n`[{}]` - `{}%`\n\n**• Size:** ( `{}` **Of** `{}` )\n\n**• ETA:** ( `{}` )"
        await event.edit(text.format(act, filename, com , percent, frem, ftotal, eta))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}

def paste(message):
    siteurl = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": message}
    headers = {
        "User-Agent": random.choice(random_headers),
        "content-type": "application/json",
    }
    response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    if response.ok:
        response = response.json()
        purl = f"https://pasty.lus.pm/{response['id']}"
        return {
            "url": purl,
            "raw": f"{purl}/raw",
        }
    else:
        return None
