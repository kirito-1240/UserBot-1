from userbot.other.emojis_index import indexs
from userbot.functions.helper import rand_string
from userbot.utils import shuffle
from PIL import Image
import random
import os
import Config
import glob

def Captcha(
    emojis=None,
    rotate=False,
    filename=None,
    count=9,
):
    new = Image.new('RGBA', (1080, 1080), (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))
    pimages = []
    emoji_names = []
    unemojis = []
    repemojis = []
    defemojis = []
    for file in glob.glob("userbot/other/emojis/*.png"):
        defemojis.append((os.path.basename(file)).replace(".png", ""))
    deffemojis = ['🃏', '🎤', '🎥', '🎨', '🎩', '🎬', '🎭', '🎮', '🎯', '🎱', '🎲', '🎷', '🎸', '🎹', '🎾', '🏀', '🏆', '🏈', '🏉', '🏐', '🏓', '💠', '💡', '💣', '💨', '💸', '💻', '💾', '💿', '📈', '📉', '📊', '📌', '📍', '📎', '📏', '📐', '📞', '📟', '📠', '📡', '📢', '📣', '📦', '📹', '📺', '📻', '📼', '📽', '🖥', '🖨', '🖲', '🗂', '🗃', '🗄', '🗜', '🗝', '🗡', '🚧', '🚨', '🛒', '🛠', '🛢', '🧀', '🌭', '🌮', '🌯', '🌺', '🌻', '🌼', '🌽', '🌾', '🌿', '🍊', '🍋', '🍌', '🍍', '🍎', '🍏', '🍚', '🍛', '🍜', '🍝', '🍞', '🍟', '🍪', '🍫', '🍬', '🍭', '🍮', '🍯', '🍺', '🍻', '🍼', '🍽', '🍾', '🍿', '🎊', '🎋', '🎍', '🎏', '🎚', '🎛', '🎞', '🐌', '🐍', '🐎', '🐚', '🐛', '🐝', '🐞', '🐟', '🐬', '🐭', '🐮', '🐯', '🐻', '🐼', '🐿', '👛', '👜', '👝', '👞', '👟', '💊', '💋', '💍', '💎', '🔋', '🔌', '🔪', '🔫', '🔬', '🔭', '🔮', '🕯', '🖊', '🖋', '🖌', '🖍', '🥚', '🥛', '🥜', '🥝', '🥞', '🦊', '🦋', '🦌', '🦍', '🦎', '🦏', '🌀', '🌂', '🌑', '🌕', '🌡', '🌤', '⛅️', '🌦', '🌧', '🌨', '🌩', '🌰', '🌱', '🌲', '🌳', '🌴', '🌵', '🌶', '🌷', '🌸', '🌹', '🍀', '🍁', '🍂', '🍃', '🍄', '🍅', '🍆', '🍇', '🍈', '🍉', '🍐', '🍑', '🍒', '🍓', '🍔', '🍕', '🍖', '🍗', '🍘', '🍙', '🍠', '🍡', '🍢', '🍣', '🍤', '🍥', '🍦', '🍧', '🍨', '🍩', '🍰', '🍱', '🍲', '🍴', '🍵', '🍶', '🍷', '🍸', '🍹', '🎀', '🎁', '🎂', '🎃', '🎄', '🎈', '🎉', '🎒', '🎓', '🎙', '🐀', '🐁', '🐂', '🐃', '🐄', '🐅', '🐆', '🐇', '🐕', '🐉', '🐓', '🐖', '🐗', '🐘', '🐙', '🐠', '🐡', '🐢', '🐣', '🐤', '🐥', '🐦', '🐧', '🐨', '🐩', '🐰', '🐱', '🐴', '🐵', '🐶', '🐷', '🐸', '🐹', '👁\u200d🗨', '👑', '👒', '👠', '👡', '👢', '💄', '💈', '🔗', '🔥', '🔦', '🔧', '🔨', '🔩', '🔰', '🔱', '🕰', '🕶', '🕹', '🖇', '🚀', '🤖', '🥀', '🥁', '🥂', '🥃', '🥐', '🥑', '🥒', '🥓', '🥔', '🥕', '🥖', '🥗', '🥘', '🥙', '🦀', '🦁', '🦂', '🦃', '🦄', '🦅', '🦆', '🦇', '🦈', '🦉', '🦐', '🦑', '⭐️', '⏰', '⏲', '⚠️', '⚡️', '⚰️', '⚽️', '⚾️', '⛄️', '⛅️', '⛈', '⛏', '⛓', '⌚️', '☎️', '⚜️', '✏️', '⌨️', '☁️', '☃️', '☄️', '☕️', '☘️', '☠️', '♨️', '⚒', '⚔️', '⚙️', '✈️', '✉️', '✒️']
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
