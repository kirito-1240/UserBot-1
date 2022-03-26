from userbot import app , bot , LOGS , LOG_GROUP
import os , sys , asyncio
from time import gmtime, strftime
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
    pattern = args.get("pattern" , None)
    info = args.get("info" , None)
    group_only = args.get("group_only" , False)
    private_only = args.get("private_only" , False)
    channel_only = args.get("channel_only" , False)
    incoming = args.get("incoming" , False)
    outgoing = args.get("outgoing" , True)
    edited = args.get("edited" , True)
    via_bot = args.get("via_bot" , False)
    fwd = args.get("fwd" , False)
    
    def decorator(func):
        async def wrapper(event):
            if via_bot and not event.via_bot_id:
                return
            if fwd and not event.fwd_from:
                return
            if group_only and not event.is_group:
                return
            if private_only and not event.is_private:
                return
            if channel_only and not event.post:
                return
            if incoming and event.out:
                return
            if outgoing and not event.out:
                return
            try:
                await func(event)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except MessageNotModifiedError:
                LOGS.info("• Sorry, Message Was Same As Previous Message!")
            except MessageIdInvalidError:
                LOGS.info("• Sorry, Message Was Deleted Or Cant Be Found!")
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
                LOGS.info(f"• Sorry, A Flood Wait Of {e.seconds} Occured. Please Wait For {e.seconds} Seconds And Try Again!")
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

async def my_id():
    return ((await app.get_me()).id)

def alien_asst(**args):
    pattern = args.get("pattern" , None)
    group_only = args.get("group_only" , False)
    private_only = args.get("private_only" , False)
    channel_only = args.get("channel_only" , False)
    incoming = args.get("incoming" , True)
    outgoing = args.get("outgoing" , False)
    me_only = args.get("me_only" , False)
    edited = args.get("edited" , True)
    via_bot = args.get("via_bot" , False)
    fwd = args.get("fwd" , False)

    def decorator(func):
        async def wrapper(event):
            if via_bot and not event.via_bot_id:
                return
            if fwd and not event.fwd_from:
                return
            if group_only and not event.is_group:
                return
            if private_only and not event.is_private:
                return
            if channel_only and not event.post:
                return
            if incoming and event.out:
                return
            if outgoing and not event.out:
                return
            if me_only and not event.from_id and not event.from_id.user_id == int(my_id()):
                return
            if me_only and not event.peer_id.user_id and not event.peer_id.user_id == int(my_id()):
                return
            try:
                await func(event)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except MessageNotModifiedError:
                LOGS.info("• Sorry, Message Was Same As Previous Message!")
            except MessageIdInvalidError:
                LOGS.info("• Sorry, Message Was Deleted Or Cant Be Found!")
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
                LOGS.info(f"• Sorry, A Flood Wait Of {e.seconds} Occured. Please Wait For {e.seconds} Seconds And Try Again!")
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
