from userbot import app, bot
from userbot.core.logger import LOGS
from userbot.utils import runcmd
from userbot.functions.core import paste
from time import gmtime, strftime
from userbot.database import DB
from traceback import format_exc
from telethon import events
import Config
from telethon.errors import (
    AlreadyInConversationError,
    BotInlineDisabledError,
    BotResponseTimeoutError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
    ChatSendStickersForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)
import os
import sys
import asyncio
import re

def alien(
    pattern=None,
    groups_only=False,
    privates_only=False,
    channels_only=False,
    outgoing=True,
    incoming=False,
    **kwargs,
):
    if pattern:
        pattern = re.compile("(?i)^\\" + Config.COMMAND_HANDLER + pattern + "$")        
    def decorator(func):
        async def wrapper(event):
            if groups_only and not event.is_group:
                return
            if privates_only and not event.is_private:
                return
            if channels_only and not event.post:
                return
            if outgoing and not event.out:
                return
            if incoming and event.out:
                return
            if event.fwd_from and event.via_bot_id:
                return
            try:
                await func(event)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except MessageNotModifiedError:
                await event.edit("`• Sorry, Message Was Same As Previous Message!`")
                await asyncio.sleep(5)
                await event.delete()
            except MessageIdInvalidError:
                await event.edit("`• Sorry, Message Was Deleted Or Cant Be Found!`")
                await asyncio.sleep(5)
                await event.delete()
            except BotInlineDisabledError:
                await event.edit("`• Sorry, Please Turn On Inline Mode For Our Bot!`")
                await asyncio.sleep(5)
                await event.delete()
            except ChatSendStickersForbiddenError:
                await event.edit("`• Sorry, Im Guess I Can't Send Stickers In This Chat!`")
                await asyncio.sleep(5)
                await event.delete()
            except BotResponseTimeoutError:
                await event.edit("`• Sorry, The Bot Didnt Answer To Your Query In Time!`")
                await asyncio.sleep(5)
                await event.delete()                    
            except ChatSendMediaForbiddenError:
                await event.edit("`• Sorry, You Can't Send Media In This Chat!`")
                await asyncio.sleep(5)
                await event.delete()
            except AlreadyInConversationError:
                await event.edit("`• Sorry, A Conversation Is Already Happening With The Given Chat. Try Again After Some Time!`")
                await asyncio.sleep(5)
                await event.delete()
            except ChatSendInlineForbiddenError:
                await event.edit("`• Sorry, You Can't Send Inline Messages In This Chat!`")
                await asyncio.sleep(5)
                await event.delete()
            except FloodWaitError as e:
                LOGS.error(f"• Sorry, A Flood Wait Of {e.seconds} Occured. Please Wait For {e.seconds} Seconds And Try Again!")
                await event.delete()
                await asyncio.sleep(e.seconds + 5)
            except:
                date = strftime("%Y-%m-%d - %H:%M:%S", gmtime())
                ftext = f"• Alien Userbot Logs •\n\n"
                ftext += f"• Date: {date}\n"
                ftext += f"• Chat ID: {event.chat_id}\n"
                ftext += f"• Sender ID: {event.sender_id}\n\n"
                ftext += f"• Event Trigger:\n {event.text}\n\n"
                ftext += f"• Traceback Info:\n {format_exc()}\n\n"
                ftext += f"• Error Text:\n {sys.exc_info()[1]}\n\n"
                gilogs = (await runcmd('git log --pretty=format:"%an: %s" -50'))[0]
                ftext += f"• Last Commits: {gilogs}"
                try:
                    await event.edit("• Sorry, Alien Userbot Has Crashed. The Error Logs Are Stored In The Alien Userbot Log Group!")
                except:
                    pass
                pas = paste(ftext)
                text = f"** • Alien Userbot Logs:** ( {pas['url']} )"
                await event.client.send_message(DB.get_key("LOG_GROUP"), text)
        app.add_event_handler(wrapper, events.MessageEdited(pattern=pattern, **kwargs))
        app.add_event_handler(wrapper, events.NewMessage(pattern=pattern, **kwargs))
        return wrapper
    return decorator
