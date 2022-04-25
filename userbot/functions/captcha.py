from userbot.other.emojis_index import indexs
from userbot.functions.helper import rand_string
from userbot.utils import shuffle
from PIL import Image
import random
import os
import Config

def get_position(count):
    if count == 6:
        position = [(5, 5), (40, 5), (75, 5), (5, 40), (40, 40), (75, 40)]
    elif count == 9:
        position = [(5, 5), (40, 5), (75, 5), (5, 40), (40, 40), (75, 40), (5, 75), (40, 75), (75, 75)]
    elif count == 12:
        position = [(5, 5), (40, 5), (75, 5), (110, 5), (5, 40), (40, 40), (75, 40), (110, 40), (5, 75), (40, 75), (75, 75), (110, 75)]
    elif count == 16:
        position = [(5, 5), (40, 5), (75, 5), (110, 5), (5, 40), (40, 40), (75, 40), (110, 40), (5, 75), (40, 75), (75, 75), (110, 75), (5, 110), (40, 110), (75, 110), (110, 110)]
    elif count == 20:
        position = [(5, 5), (40, 5), (75, 5), (110, 5), (5, 40), (40, 40), (75, 40), (110, 40), (5, 75), (40, 75), (75, 75), (110, 75), (5, 110), (40, 110), (75, 110), (110, 110), (5, 145), (40, 145), (75, 145), (110, 145)]
    return position

def get_size(count):
    if count == 6:
        size = (111, 75)
    elif count == 9:
        size = (110, 110)
    elif count == 12:
        size = (146, 112)
    elif count == 16:
        size = (148, 140)
    elif count == 20:
        size = (148, 170)
    return size

def Captcha(
    background=None,
    emojis=None,
    rotate=False,
    filename=None,
    count=9,
):
    if count not in [6, 9, 12, 16, 20]:
        count = 12
    imsize = get_size(count)
    if background:
        new = Image.open(background)
        new = new.resize(imsize)
    else:
        new = Image.new('RGBA', imsize, (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))
    pimages = []
    emoji_names = []
    unemojis = []
    repemojis = []
    defemojis = ['🃏', '🎤', '🎥', '🎨', '🎩', '🎬', '🎭', '🎮', '🎯', '🎱', '🎲', '🎷', '🎸', '🎹', '🎾', '🏀', '🏆', '🏈', '🏉', '🏐', '🏓', '💠', '💡', '💣', '💨', '💸', '💻', '💾', '💿', '📈', '📉', '📊', '📌', '📍', '📎', '📏', '📐', '📞', '📟', '📠', '📡', '📢', '📣', '📦', '📹', '📺', '📻', '📼', '📽', '🖥', '🖨', '🖲', '🗂', '🗃', '🗄', '🗜', '🗝', '🗡', '🚧', '🚨', '🛒', '🛠', '🛢', '🧀', '🌭', '🌮', '🌯', '🌺', '🌻', '🌼', '🌽', '🌾', '🌿', '🍊', '🍋', '🍌', '🍍', '🍎', '🍏', '🍚', '🍛', '🍜', '🍝', '🍞', '🍟', '🍪', '🍫', '🍬', '🍭', '🍮', '🍯', '🍺', '🍻', '🍼', '🍽', '🍾', '🍿', '🎊', '🎋', '🎍', '🎏', '🎚', '🎛', '🎞', '🐌', '🐍', '🐎', '🐚', '🐛', '🐝', '🐞', '🐟', '🐬', '🐭', '🐮', '🐯', '🐻', '🐼', '🐿', '👛', '👜', '👝', '👞', '👟', '💊', '💋', '💍', '💎', '🔋', '🔌', '🔪', '🔫', '🔬', '🔭', '🔮', '🕯', '🖊', '🖋', '🖌', '🖍', '🥚', '🥛', '🥜', '🥝', '🥞', '🦊', '🦋', '🦌', '🦍', '🦎', '🦏', '🌀', '🌂', '🌑', '🌕', '🌡', '🌤', '⛅️', '🌦', '🌧', '🌨', '🌩', '🌰', '🌱', '🌲', '🌳', '🌴', '🌵', '🌶', '🌷', '🌸', '🌹', '🍀', '🍁', '🍂', '🍃', '🍄', '🍅', '🍆', '🍇', '🍈', '🍉', '🍐', '🍑', '🍒', '🍓', '🍔', '🍕', '🍖', '🍗', '🍘', '🍙', '🍠', '🍡', '🍢', '🍣', '🍤', '🍥', '🍦', '🍧', '🍨', '🍩', '🍰', '🍱', '🍲', '🍴', '🍵', '🍶', '🍷', '🍸', '🍹', '🎀', '🎁', '🎂', '🎃', '🎄', '🎈', '🎉', '🎒', '🎓', '🎙', '🐀', '🐁', '🐂', '🐃', '🐄', '🐅', '🐆', '🐇', '🐕', '🐉', '🐓', '🐖', '🐗', '🐘', '🐙', '🐠', '🐡', '🐢', '🐣', '🐤', '🐥', '🐦', '🐧', '🐨', '🐩', '🐰', '🐱', '🐴', '🐵', '🐶', '🐷', '🐸', '🐹', '👁\u200d🗨', '👑', '👒', '👠', '👡', '👢', '💄', '💈', '🔗', '🔥', '🔦', '🔧', '🔨', '🔩', '🔰', '🔱', '🕰', '🕶', '🕹', '🖇', '🚀', '🤖', '🥀', '🥁', '🥂', '🥃', '🥐', '🥑', '🥒', '🥓', '🥔', '🥕', '🥖', '🥗', '🥘', '🥙', '🦀', '🦁', '🦂', '🦃', '🦄', '🦅', '🦆', '🦇', '🦈', '🦉', '🦐', '🦑', '⭐️', '⏰', '⏲', '⚠️', '⚡️', '⚰️', '⚽️', '⚾️', '⛄️', '⛅️', '⛈', '⛏', '⛓', '⌚️', '☎️', '⚜️', '✏️', '⌨️', '☁️', '☃️', '☄️', '☕️', '☘️', '☠️', '♨️', '⚒', '⚔️', '⚙️', '✈️', '✉️', '✒️']
    if not emojis:
        emojis = defemojis
    for i in range(count):
        rand = random.choice(emojis)
        index = indexs.get(rand)
        file = os.path.join("userbot/other/emojis/",  f"{index}.png")
        if not os.path.exists(file):
            emojis.remove(rand)
            unemojis.append(rand)
            rands = random.choice(defemojis)
            emoji_names.append(rands)
            repemojis.append(rands)
            inde = indexs.get(rands)
            file = os.path.join("userbot/other/emojis/",  f"{inde}.png")
            pimages.append(file)
        else:
            emoji_names.append(rand) 
            pimages.append(file)
            emojis.remove(rand)
    position = get_position(count)
    for i in range(len(pimages)):
        img = Image.open(pimages[i])
        if rotate:
            img = img.rotate(random.randint(0, 360), resample=Image.BICUBIC, expand=True)
        img.thumbnail((30,30), Image.ANTIALIAS)
        new.paste(img, (position[i]), img)
    outfile = filename if filename else os.path.join("userbot/other/emojis/",  rand_string() + ".png")
    new.save(outfile, "PNG", quality=95)
    return {"answer": emoji_names, "others": emojis, "unavailables": unemojis, "repleyes": repemojis, "captcha": outfile}
