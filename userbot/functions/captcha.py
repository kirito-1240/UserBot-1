from userbot.other.emojis_index import indexs
from userbot.other.emojis_name import names
from userbot.other.allemojis import emojis as allemojis
from userbot.functions.helper import rand_string
from userbot.utils import shuffle
from PIL import Image
from userbot import Config
import random
import requests
import os
import glob

def Captcha(
    emojis=None,
    rotate=False,
    filename=None,
    count=8,
):
    new = Image.new('RGBA', (1080, 1080), (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))
    pimages = []
    emoji_names = []
    unemojis = []
    repemojis = []
    if not emojis:
        emojis = allemojis
    if count > len(emojis):
        count = len(emojis)
    for i in range(count):
        rand = random.choice(emojis)
        name = names.get(rand)
        key = random.choice(["4b57243e05f7036bc3b39c5052f55d2f085f6e6", "409ec6811a7a81d9f35bd188075b1e292388d316", "f8b2353b057e8879b5e1f63aeaa10ee9772f72b7"])
        index = (requests.get(f"https://emoji-api.com/emojis?search={name}&access_key={key}").r.json().r[0]['codePoint']).lower()
        file = os.path.join("userbot/other/emojis/",  f"{index}.png")
        if not os.path.exists(file):
            rand = random.choice(allemojis)
            emoji_names.append(rand) 
            pimages.append(file)
            emojis.remove(rand)
        else:
            emojis.remove(rand)
            unemojis.append(rand)
            rands = random.choice(defemojis)
            emoji_names.append(rands)
            repemojis.append(rands)
            inde = indexs.get(rands)
            file = os.path.join("userbot/other/emojis/",  f"{inde}.png")
            pimages.append(file)
    for i in range(len(pimages)):
        img = Image.open(pimages[i])
        if rotate:
            img = img.rotate(random.randint(0, 360))
        img.thumbnail((200, 200), Image.ANTIALIAS)
        position = (random.randint(0, 900), random.randint(0, 900))
        new.paste(img, (position), img)
    outfile = filename if filename else os.path.join("userbot/other/emojis/",  rand_string() + ".png")
    new.save(outfile, "PNG")
    return {
        "answer": emoji_names,
        "others": emojis,
        "unavailables": unemojis,
        "repleyes": repemojis,
        "captcha": outfile
    }
