from userbot.functions.tools import download_file, get_emoji_link, get_emoji_code
from userbot.other.emojis_index import indexs
from userbot.functions.helper import rand_string
from userbot.functions.github import GITAPP
from userbot.utils import shuffle
from userbot import Config
from PIL import Image
import random
import os
import glob 

async def Captcha(
    emojis=None,
    rotate=False,
    filename=None,
    count=8,
    emojisize=(200, 200),
):
    new = Image.new('RGBA', (1080, 1080), (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))
    pimages = []
    answers = []
    if not emojis:
        emojis = []
        for f in indexs:
            emojis.append(f)
    if count > len(emojis):
        count = len(emojis)
    for i in range(count):
        rand = random.choice(emojis)
        index = rand
        if emojis:
            index = indexs.get(rand)
            if not index:
                index = await get_emoji_code(rand)
        file = os.path.join("userbot/other/emojis/",  f"{index}.png")
        if os.path.exists(file):
            answers.append(rand) 
            emojis.remove(rand)
        else:
            try:
                link = await get_emoji_link(rand)
                filepath = os.path.join("userbot/other/emojis/",  f"{index}.png")
                filepath = await download_file(link, file)
                GITAPP().create(filepath, filepath)
                answers.append(rand) 
                pimages.append(filepath)
                emojis.remove(rand)
            except:
                emojis.remove(rand)
                rands = random.choice(emojis)
                answers.append(rands)
                inde = indexs.get(rands)
                file = os.path.join("userbot/other/emojis/",  f"{inde}.png")
                pimages.append(file)
    for i in range(len(pimages)):
        img = Image.open(pimages[i])
        if rotate:
            img = img.rotate(random.randint(0, 360))
        img.thumbnail((emojisize), Image.ANTIALIAS)
        position = (random.randint(0, 900), random.randint(0, 900))
        new.paste(img, (position), img)
    outfile = filename if filename else os.path.join("userbot/other/emojis/",  rand_string() + ".png")
    new.save(outfile, "PNG")
    return {
        "answers": answers,
        "others": emojis,
        "captcha": outfile
    }
