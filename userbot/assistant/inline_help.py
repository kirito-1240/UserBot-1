import re
import time
from datetime import datetime
from os import remove

from git import Repo
from pyUltroid._misc._assistant import callback, in_pattern
from pyUltroid.dB._core import HELP, LIST
from pyUltroid.functions.helper import gen_chlog, time_formatter, updater
from pyUltroid.functions.misc import split_list
from telethon import Button
from telethon.tl.types import InputWebDocument, Message
from telethon.utils import resolve_bot_file_id

from . import HNDLR, INLINE_PIC, LOGS, OWNER_NAME, asst, get_string, start_time, udB
from ._help import _main_help_menu

# ================================================#

TLINK = INLINE_PIC or "https://telegra.ph/file/74d6259983e0642923fdb.jpg"
helps = get_string("inline_1")

add_ons = udB.get_key("ADDONS")

if add_ons is not False:
    zhelps = get_string("inline_2")
else:
    zhelps = get_string("inline_3")

PLUGINS = HELP.get("Official", [])
ADDONS = HELP.get("Addons", [])
upage = 0


def page_num(index):
    rows = 5
    cols = 2
    emoji = "•"
    files = glob.glob("userbot/plugins/*.py")
    plugin_list = []
    for file in sorted(files):
        name = os.path.basename(file).replace(".py" , "")
        plugin_list.append(str(name.title()))
    List = [
        Button.inline(f"{emoji} {key} {emoji}", data=f"help_plugin_{key}")
        for key in sorted(plugin_list)
    ]
    all = split_list(List, cols)
    fl = split_list(all, rows)
        new_.append(
            [
                Button.inline(
                    "« Pʀᴇᴠɪᴏᴜs",
                    data=f"uh_{key}_{index-1}",
                ),
                Button.inline("« Bᴀᴄᴋ »", data="open"),
                Button.inline(
                    "Nᴇxᴛ »",
                    data=f"uh_{key}_{index+1}",
                ),
            ]
        )
    return new_

@alien_callback("page_(.*)", owner=True)
async def help_func(event):
    files = glob.glob("userbot/plugins/*.py")
    plugin_list = []
    for file in sorted(files):
        name = os.path.basename(file).replace(".py" , "")
        plugin_list.append(str(name.title()))
    pages = event.data_match.group(1).decode("utf-8")
    page = int(f"{pages}0")
    if page == 00:
        main = plugin_list[0:10]
    else:
        try:
            main = plugin_list[page:(page + 10)]
        except:
            main = plugin_list[page:int(len(plugin_list))]
    list = [
        Button.inline(f"{key}", data=f"help_plugin_{key}")
        for key in sorted(main)
    ]
    all = split_list(list, 2)
    fl = split_list(all, 5)
    if not page > int(len(plugin_list)):
        list.append([Button.inline("Next", data=f"page_{int(pages)+1}")])
    if not page == 00:
        list.append([Button.inline("Back", data=f"page_{int(pages)-1}")])

@alien_callback("alien_inline_help", owner=True)
async def help_func(event):
    files = glob.glob("userbot/plugins/*.py")
    plugin_list = []
    for file in sorted(files):
        name = os.path.basename(file).replace(".py" , "")
        plugin_list.append(str(name.title()))
    count = len(plugin_list)
    await event.edit(str(count), buttons=page_num(round(count / 10)))


@alien_callback("help_plugin_(.*)", owner=True)
async def uptd_plugin(event):
    file = event.data_match.group(1).decode("utf-8").split("_")
    buttons = []
    help = f"Help For {file}"
    buttons.append([Button.inline("• Sᴇɴᴅ Pʟᴜɢɪɴ •", data=f"sendplugin_{file}")])
    buttons.append([Button.inline("• Bᴀᴄᴋ •", data="alien_inline_help")])
    await event.edit(help, buttons=buttons)


@callback(data="doupdate", owner=True)
async def _(event):
    if not await updater():
        return await event.answer(get_string("inline_9"), cache_time=0, alert=True)
    if not INLINE_PIC:
        return await event.answer(f"Do '{HNDLR}update' to update..")
    repo = Repo.init()
    changelog, tl_chnglog = await gen_chlog(
        repo, f"HEAD..upstream/{repo.active_branch}"
    )
    changelog_str = changelog + "\n\n" + get_string("inline_8")
    if len(changelog_str) > 1024:
        await event.edit(get_string("upd_4"))
        with open("ultroid_updates.txt", "w+") as file:
            file.write(tl_chnglog)
        await event.edit(
            get_string("upd_5"),
            file="ultroid_updates.txt",
            buttons=[
                [Button.inline("• Uᴘᴅᴀᴛᴇ Nᴏᴡ •", data="updatenow")],
                [Button.inline("« Bᴀᴄᴋ", data="ownr")],
            ],
        )
        remove("ultroid_updates.txt")
    else:
        await event.edit(
            changelog_str,
            buttons=[
                [Button.inline("Update Now", data="updatenow")],
                [Button.inline("« Bᴀᴄᴋ", data="ownr")],
            ],
            parse_mode="html",
        )


@callback(data="pkng", owner=True)
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds
    pin = f"🌋Pɪɴɢ = {ms} microseconds"
    await event.answer(pin, cache_time=0, alert=True)


@callback(data="upp", owner=True)
async def _(event):
    uptime = time_formatter((time.time() - start_time) * 1000)
    pin = f"🙋Uᴘᴛɪᴍᴇ = {uptime}"
    await event.answer(pin, cache_time=0, alert=True)


@callback(data="inlone", owner=True)
async def _(e):
    button = [
        [
            Button.switch_inline(
                "Pʟᴀʏ Sᴛᴏʀᴇ Aᴘᴘs",
                query="app telegram",
                same_peer=True,
            ),
            Button.switch_inline(
                "Mᴏᴅᴅᴇᴅ Aᴘᴘs",
                query="mods minecraft",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "Sᴇᴀʀᴄʜ Oɴ Gᴏᴏɢʟᴇ",
                query="go TeamUltroid",
                same_peer=True,
            ),
            Button.switch_inline(
                "Search on XDA",
                query="xda telegram",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "WʜɪSᴘᴇʀ",
                query="wspr @username Hello🎉",
                same_peer=True,
            ),
            Button.switch_inline(
                "YᴏᴜTᴜʙᴇ Dᴏᴡɴʟᴏᴀᴅᴇʀ",
                query="yt Ed Sheeran Perfect",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "Piston Eval",
                query="run javascript console.log('Hello Ultroid')",
                same_peer=True,
            ),
            Button.switch_inline(
                "OʀᴀɴɢᴇFᴏx🦊",
                query="ofox beryllium",
                same_peer=True,
            ),
        ],
        [
            Button.switch_inline(
                "Tᴡɪᴛᴛᴇʀ Usᴇʀ", query="twitter theultroid", same_peer=True
            ),
            Button.switch_inline(
                "Kᴏᴏ Sᴇᴀʀᴄʜ", query="koo @__kumar__amit", same_peer=True
            ),
        ],
        [
            Button.switch_inline(
                "Fᴅʀᴏɪᴅ Sᴇᴀʀᴄʜ", query="fdroid telegram", same_peer=True
            ),
            Button.switch_inline("Sᴀᴀᴠɴ sᴇᴀʀᴄʜ", query="saavn", same_peer=True),
        ],
        [
            Button.switch_inline("Tʟ Sᴇᴀʀᴄʜ", query="tl", same_peer=True),
            Button.switch_inline("GɪᴛHᴜʙ ғᴇᴇᴅs", query="gh", same_peer=True),
        ],
        [Button.switch_inline("OᴍɢUʙᴜɴᴛᴜ", query="omgu cutefish", same_peer=True)],
        [
            Button.inline(
                "« Bᴀᴄᴋ",
                data="open",
            ),
        ],
    ]
    await e.edit(buttons=button, link_preview=False)


@callback(data="open", owner=True)
async def opner(event):
    z = []
    for x in LIST.values():
        z.extend(x)
    await event.edit(
        get_string("inline_4").format(
            OWNER_NAME,
            len(HELP.get("Official", [])),
            len(HELP.get("Addons", [])),
            len(z),
        ),
        buttons=_main_help_menu,
        link_preview=False,
    )


@callback(data="close", owner=True)
async def on_plug_in_callback_query_handler(event):
    await event.edit(
        get_string("inline_5"),
        buttons=Button.inline("Oᴘᴇɴ Aɢᴀɪɴ", data="open"),
    )


def page_num(index, key):
    rows = udB.get_key("HELP_ROWS") or 5
    cols = udB.get_key("HELP_COLUMNS") or 2
    loaded = HELP.get(key, [])
    emoji = udB.get_key("EMOJI_IN_HELP") or "✘"
    List = [
        Button.inline(f"{emoji} {x} {emoji}", data=f"uplugin_{key}_{x}|{index}")
        for x in sorted(loaded)
    ]
    all_ = split_list(List, cols)
    fl_ = split_list(all_, rows)
    try:
        new_ = fl_[index]
    except IndexError:
        new_ = fl_[0] if fl_ else []
        index = 0
    if index == 0 and len(fl_) == 1:
        new_.append([Button.inline("« Bᴀᴄᴋ »", data="open")])
    else:
        new_.append(
            [
                Button.inline(
                    "« Pʀᴇᴠɪᴏᴜs",
                    data=f"uh_{key}_{index-1}",
                ),
                Button.inline("« Bᴀᴄᴋ »", data="open"),
                Button.inline(
                    "Nᴇxᴛ »",
                    data=f"uh_{key}_{index+1}",
                ),
            ]
        )
    return new_


# --------------------------------------------------------------------------------- #


STUFF = {}


@in_pattern("stf(.*)", owner=True)
async def ibuild(e):
    n = e.pattern_match.group(1).strip()
    builder = e.builder
    if not (n and n.isdigit()):
        return
    ok = STUFF.get(int(n))
    txt = ok.get("msg")
    pic = ok.get("media")
    btn = ok.get("button")
    if not (pic or txt):
        txt = "Hey!"
    if pic:
        try:
            include_media = True
            mime_type, _pic = None, None
            cont, results = None, None
            try:
                ext = str(pic).split(".")[-1].lower()
            except BaseException:
                ext = None
            if ext in ["img", "jpg", "png"]:
                _type = "photo"
                mime_type = "image/jpg"
            elif ext in ["mp4", "mkv", "gif"]:
                mime_type = "video/mp4"
                _type = "gif"
            else:
                try:
                    if "telethon.tl.types" in str(type(pic)):
                        _pic = pic
                    else:
                        _pic = resolve_bot_file_id(pic)
                except BaseException:
                    pass
                if _pic:
                    results = [
                        await builder.document(
                            _pic,
                            title="Ultroid Op",
                            text=txt,
                            description="@TheUltroid",
                            buttons=btn,
                            link_preview=False,
                        )
                    ]
                else:
                    _type = "article"
                    include_media = False
            if not results:
                if include_media:
                    cont = InputWebDocument(pic, 0, mime_type, [])
                results = [
                    await builder.article(
                        title="Ultroid Op",
                        type=_type,
                        text=txt,
                        description="@TeamUltroid",
                        include_media=include_media,
                        buttons=btn,
                        thumb=cont,
                        content=cont,
                        link_preview=False,
                    )
                ]
            return await e.answer(results)
        except Exception as er:
            LOGS.exception(er)
    result = [
        await builder.article("Ultroid Op", text=txt, link_preview=False, buttons=btn)
    ]
    await e.answer(result)


async def something(e, msg, media, button, reply=True, chat=None):
    if e.client._bot:
        return await e.reply(msg, file=media, buttons=button)
    num = len(STUFF) + 1
    STUFF.update({num: {"msg": msg, "media": media, "button": button}})
    try:
        res = await e.client.inline_query(asst.me.username, f"stf{num}")
        return await res[0].click(
            chat or e.chat_id,
            reply_to=bool(isinstance(e, Message) and reply),
            hide_via=True,
            silent=True,
        )

    except Exception as er:
        LOGS.exception(er)
