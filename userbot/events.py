from userbot import app , bot , LOGS , LOG_GROUP
import os , sys , asyncio
from time import gmtime, strftime
from userbot.database import DB
from traceback import format_exc
from telethon import events
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

def alien(**args):
    pattern = args.get("pattern", None)
    groups_only = args.get("groups_only", False)
    privates_only = args.get("privates_only", False)
    channels_only = args.get("channels_only", False)
    outgoing = args.get("outgoing", True)
    incoming = args.get("incoming", False)
    edited = args.get("edited", True)

    if "groups_only" in args:
        del args['groups_only']
    if "privates_only" in args:
        del args['privates_only']
    if "channels_only" in args:
        del args['channels_only']
    if "outgoing" in args:
        del args['outgoing']
    if "incoming" in args:
        del args['incoming']      
    if "edited" in args:
        del args['edited']

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
                ftext = "**• Alien Userbot Logs •**\n\n"
                ftext += f"**• Date:** `{date}`\n"
                ftext += f"**• Chat ID:** `{event.chat_id}`\n"
                ftext += f"**• Sender ID:** `{event.sender_id}`\n\n"
                ftext += f"**• Event Trigger:**\n `{event.text}`\n\n"
                ftext += f"**• Traceback Info:**\n `{format_exc()}`\n\n"
                ftext += f"**• Error Text:**\n `{sys.exc_info()[1]}`"
                await event.edit("`• Sorry, Alien Userbot Has Crashed. The Error Logs Are Stored In The Alien Userbot Log Group!`")
                await event.client.send_message(LOG_GROUP , ftext)
        if edited:
            app.add_event_handler(wrapper, events.MessageEdited(**args))
        app.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper
    return decorator

def alien_asst(**args):
    pattern = args.get("pattern", None)
    groups_only = args.get("groups_only", False)
    privates_only = args.get("privates_only", False)
    channels_only = args.get("channels_only", False)
    outgoing = args.get("outgoing", True)
    incoming = args.get("incoming", False)
    edited = args.get("edited", True)

    if "groups_only" in args:
        del args['groups_only']
    if "privates_only" in args:
        del args['privates_only']
    if "channels_only" in args:
        del args['channels_only']
    if "outgoing" in args:
        del args['outgoing']
    if "incoming" in args:
        del args['incoming']      
    if "edited" in args:
        del args['edited']

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
                await event.reply("`• Sorry, Please Turn On Inline Mode For Our Bot!`")
                await asyncio.sleep(5)
                await event.delete()
            except ChatSendStickersForbiddenError:
                await event.reply("`• Sorry, Im Guess I Can't Send Stickers In This Chat!`")
                await asyncio.sleep(5)
                await event.delete()
            except BotResponseTimeoutError:
                await event.reply("`• Sorry, The Bot Didnt Answer To Your Query In Time!`")
                await asyncio.sleep(5)
                await event.delete()                    
            except ChatSendMediaForbiddenError:
                await event.reply("`• Sorry, You Can't Send Media In This Chat!`")
                await asyncio.sleep(5)
                await event.delete()
            except AlreadyInConversationError:
                await event.reply("`• Sorry, A Conversation Is Already Happening With The Given Chat. Try Again After Some Time!`")
                await asyncio.sleep(5)
                await event.delete()
            except ChatSendInlineForbiddenError:
                await event.reply("`• Sorry, You Can't Send Inline Messages In This Chat!`")
                await asyncio.sleep(5)
                await event.delete()
            except FloodWaitError as e:
                LOGS.error(f"• Sorry, A Flood Wait Of {e.seconds} Occured. Please Wait For {e.seconds} Seconds And Try Again!")
                await event.delete()
                await asyncio.sleep(e.seconds + 5)
            except:
                date = strftime("%Y-%m-%d - %H:%M:%S", gmtime())
                ftext = "**• Alien Assian Logs •**\n\n"
                ftext += f"**• Date:** `{date}`\n"
                ftext += f"**• Chat ID:** `{event.chat_id}`\n"
                ftext += f"**• Sender ID:** `{event.sender_id}`\n\n"
                ftext += f"**• Event Trigger:**\n `{event.text}`\n\n"
                ftext += f"**• Traceback Info:**\n `{format_exc()}`\n\n"
                ftext += f"**• Error Text:**\n `{sys.exc_info()[1]}`"
                await event.reply("`• Sorry, Alien Assistantbot Has Crashed. The Error Logs Are Stored In The Alien Assistantbot Log Group!`")
                await event.client.send_message(LOG_GROUP , ftext) 
        if edited:
            bot.add_event_handler(wrapper, events.MessageEdited(**args))
        bot.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper
    return decorator
