from userbot.other.emojis_index import indexs
from userbot.other.all_emojis import emojis
from userbot.functions.helper import rand_string
from userbot.functions.tools import downloadfile
from userbot.functions.github import GITAPP
from userbot.utils import shuffle
from PIL import Image
import random
import os
import Config

def Captcha():
    new = Image.new('RGB', (430, 415), (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))
    pimages = []
    emoji_names = []
    emojis = emojis
    emojis = shuffle(emojis)
    others = emojis
    for i in range(9):
        index = emojis_index.get(emojis[i])
        file = os.path.join(f"{Config.CURRENT_DIR}/userbot/other/emojis/",  f"{index}.png")
        if not os.path.exists(file):
            link = "https://emoji.aranja.com/static/emoji-data/img-apple-160/{}.png".format(index)
            try:
                last = downloadfile(link, file)
                gapp = GITAPP()
                gapp.create(last, f"./userbot/other/emojis/{index}.png")
            except Exception as e:
                print(e)
                continue
        emoji_names.append(emojis[i]) 
        pimages.append(file)
        others.remove(emojis[i])
    position = [(20, 20), (160, 20), (300, 20), (20, 160), (160, 160), (300, 160), (20, 300), (160, 300), (300, 300)]
    for i in range(len(pimages)):
        img = Image.open(pimages[i]).rotate(random.randint(0, 360), resample=Image.BICUBIC, expand=True)
        img.thumbnail((100, 100), Image.ANTIALIAS)
        new.paste(img, (position[i]), img)
    newpath = os.path.join(f"{Config.CURRENT_DIR}/userbot/other/emojis/",  rand_string() + ".png")
    new.save(newpath, "PNG")
    return {"answer": emoji_names, "others": others, "captcha": newpath}
