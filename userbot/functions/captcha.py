from userbot.other.emojis_index import indexs
from userbot.other.emojis_link import links
from userbot.other.emojis import emojis as allemojis
from userbot.functions.helper import rand_string
from userbot.functions.tools import download_file
from userbot.utils import shuffle
from PIL import Image
from userbot import Config
import random
import requests
import os
import glob
from userbot.functions.tools import get_emoji_link, get_emoji_code

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
    defemojis = ['😀', '😃', '😄', '😁', '😆', '😅', '🤣', '😂', '🙂', '🙃', '😉', '😊', '😇', '😍', '😘', '😗', '😚', '😙', '😋', '😛', '😜', '😝', '🤑', '🤗', '🤔', '🤐', '😐', '😑', '😶', '😏', '😒', '🙄', '😬', '🤥', '😌', '😔', '😪', '🤤', '😴', '😷', '🤒', '🤕', '🤢', '🤧', '😵', '🤠', '😎', '🤓', '😕', '😟', '🙁', '😮', '😯', '😲', '😳', '😦', '😧', '😨', '😰', '😥', '😢', '😭', '😱', '😖', '😣', '😞', '😓', '😩', '😫', '😤', '😡', '🃏', '🎤', '🎥', '🎨', '🎩', '🎬', '🎭', '🎮', '🎯', '🎱', '🎲', '🎷', '🎸', '🎹', '🎾', '🏀', '🏆', '🏈', '🏉', '🏐', '🏓', '💠', '💡', '💣', '💨', '💸', '💻', '💾', '💿', '📈', '📉', '📊', '📌', '📍', '📎', '📏', '📐', '📞', '📟', '📠', '📡', '📢', '📣', '📦', '📹', '📺', '📻', '📼', '📽', '🖥', '🖨', '🖲', '🗂', '🗃', '🗄', '🗜', '🗝', '🗡', '🚧', '🚨', '🛒', '🛠', '🛢', '🧀', '🌭', '🌮', '🌯', '🌺', '🌻', '🌼', '🌽', '🌾', '🌿', '🍊', '🍋', '🍌', '🍍', '🍎', '🍏', '🍚', '🍛', '🍜', '🍝', '🍞', '🍟', '🍪', '🍫', '🍬', '🍭', '🍮', '🍯', '🍺', '🍻', '🍼', '🍽', '🍾', '🍿', '🎊', '🎋', '🎍', '🎏', '🎚', '🎛', '🎞', '🐌', '🐍', '🐎', '🐚', '🐛', '🐝', '🐞', '🐟', '🐬', '🐭', '🐮', '🐯', '🐻', '🐼', '🐿', '👛', '👜', '👝', '👞', '👟', '💊', '💋', '💍', '💎', '🔋', '🔌', '🔪', '🔫', '🔬', '🔭', '🔮', '🕯', '🖊', '🖋', '🖌', '🖍', '🥚', '🥛', '🥜', '🥝', '🥞', '🦊', '🦋', '🦌', '🦍', '🦎', '🦏', '🌀', '🌂', '🌑', '🌕', '🌡', '🌤', '⛅️', '🌦', '🌧', '🌨', '🌩', '🌰', '🌱', '🌲', '🌳', '🌴', '🌵', '🌶', '🌷', '🌸', '🌹', '🍀', '🍁', '🍂', '🍃', '🍄', '🍅', '🍆', '🍇', '🍈', '🍉', '🍐', '🍑', '🍒', '🍓', '🍔', '🍕', '🍖', '🍗', '🍘', '🍙', '🍠', '🍡', '🍢', '🍣', '🍤', '🍥', '🍦', '🍧', '🍨', '🍩', '🍰', '🍱', '🍲', '🍴', '🍵', '🍶', '🍷', '🍸', '🍹', '🎀', '🎁', '🎂', '🎃', '🎄', '🎈', '🎉', '🎒', '🎓', '🎙', '🐀', '🐁', '🐂', '🐃', '🐄', '🐅', '🐆', '🐇', '🐕', '🐉', '🐓', '🐖', '🐗', '🐘', '🐙', '🐠', '🐡', '🐢', '🐣', '🐤', '🐥', '🐦', '🐧', '🐨', '🐩', '🐰', '🐱', '🐴', '🐵', '🐶', '🐷', '🐸', '🐹', '👁\u200d🗨', '👑', '👒', '👠', '👡', '👢', '💄', '💈', '🔗', '🔥', '🔦', '🔧', '🔨', '🔩', '🔰', '🔱', '🕰', '🕶', '🕹', '🖇', '🚀', '🤖', '🥀', '🥁', '🥂', '🥃', '🥐', '🥑', '🥒', '🥓', '🥔', '🥕', '🥖', '🥗', '🥘', '🥙', '🦀', '🦁', '🦂', '🦃', '🦄', '🦅', '🦆', '🦇', '🦈', '🦉', '🦐', '🦑', '⭐️', '⏰', '⏲', '⚠️', '⚡️', '⚰️', '⚽️', '⚾️', '⛄️', '⛅️', '⛈', '⛏', '⛓', '⌚️', '☎️', '⚜️', '✏️', '⌨️', '☁️', '☃️', '☄️', '☕️', '☘️', '☠️', '♨️', '⚒', '⚔️', '⚙️', '✈️', '✉️', '✒️']
    if count > len(emojis):
        count = len(emojis)
    for i in range(count):
        rand = random.choice(emojis)
        index = indexs.get(rand)
        file = os.path.join("userbot/other/emojis/",  f"{index}.png")
        if os.path.exists(file):
            emoji_names.append(rand) 
            pimages.append(file)
            emojis.remove(rand)
        else:
            try:
                link = links.get(index)
                filepath = os.path.join("userbot/other/emojis/",  f"{index}.png")
                filepath = downloadfile(link, file)
                emoji_names.append(rand) 
                pimages.append(filepath)
                emojis.remove(rand)
            except:
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
        "unavailables": unemojis,
        "repleyes": repemojis,
        "others": emojis,
        "captcha": outfile
    }

async def Captchaa(
    emojis=None,
    rotate=False,
    filename=None,
    count=8,
):
    new = Image.new('RGBA', (1080, 1080), (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))
    pimages = []
    emoji_names = []
    if not emojis:
        emojis = allemojis
    if count > len(emojis):
        count = len(emojis)
    for i in range(count):
        rand = random.choice(emojis)
        link = await get_emoji_link(rand)
        filepath = os.path.join("userbot/other/",  f"{rand}.png")
        filepath = await download_file(link, filepath)
        emoji_names.append(rand) 
        pimages.append(filepath)
        emojis.remove(rand)
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
        "captcha": outfile
    }
