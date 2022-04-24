import os
import random
from PIL import Image
from userbot.utils import shuffle
from userbot.other.emojis_index import emojis_index
from userbot.functions.tools import downloadfile

def Captcha():
    new = Image.new('RGB', (430, 415), (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))
    paste_image_list = list()
    emoji_names = list()
    supported_emojis = []
    for em in emojis_index:
        supported_emojis.append(em) 
    supported_emojis = shuffle(supported_emojis)
    others = supported_emojis
    for i in range(9):
        others.remove(supported_emojis[i])
        emoji_names.append(supported_emojis[i])
        index = emojis_index.get(supported_emojis[i])
        link = f"https://emoji.aranja.com/static/emoji-data/img-apple-160/{index}.png" 
        file = downloadfile(link, f"cache/{index}.png")
        paste_image_list.append(os.path.join("cache", file))
    position = [(20, 20), (160, 20), (300, 20), (20, 160), (160, 160), (300, 160), (20, 300), (160, 300), (300, 300)]
    for i in range(len(paste_image_list)):
        img = Image.open(paste_image_list[i]).rotate(random.randint(0, 360), resample=Image.BICUBIC, expand=True)
        img.thumbnail((100, 100), Image.ANTIALIAS)
        new.paste(img, (position[i]), img)
    emoji_captcha_path = os.path.join("cache", emojis_index.get(supported_emojis[i]) + ".png")
    new.save(emoji_captcha_path, "PNG")
    return {"answer": emoji_names, "others": others, "captcha": emoji_captcha_path}
