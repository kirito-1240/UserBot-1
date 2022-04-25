from userbot.other.emojis_index import indexs
from userbot.functions.helper import rand_string
from userbot.utils import shuffle
from PIL import Image
import random
import os
import Config

def get_position(count):
    if count == 4:
        position = [(20, 20), (70, 20), (20, 70), (70, 70)]
    elif count == 6:
        position = [(20, 20), (70, 20), (120, 20), (20, 70), (70, 70), (120, 70)]
    elif count == 9:
        position = [(20, 20), (70, 20), (120, 20), (20, 70), (70, 70), (120, 70), (20, 120), (70, 120), (120, 120)]
    return position

def get_size(count):
    if count == 4:
        size = (100, 100)
    elif count == 6:
        size = (150, 150)
    elif count == 9:
        size = (200, 200)
    return size

def Captcha(
    background=None,
    emojis=None,
    rotate=True,
    filename=None,
    count=9,
):
    if count not in [4, 6, 9, 12, 15, 16, 20]:
        count = 12
    imsize = (360, 360)
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
    size = get_size(count)
    for i in range(len(pimages)):
        img = Image.open(pimages[i])
        if rotate:
            img = img.rotate(random.randint(0, 360), resample=Image.BICUBIC, expand=True)
        img.thumbnail(size, Image.ANTIALIAS)
        new.paste(img, (position[i]), img)
    outfile = filename if filename else os.path.join("userbot/other/emojis/",  rand_string() + ".png")
    new.save(outfile, "PNG")
    return {"answer": emoji_names, "others": emojis, "unavailables": unemojis, "repleyes": repemojis, "captcha": outfile}
