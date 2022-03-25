from userbot import app , LOGS , LOG_GROUP
from asyncio import create_subprocess_exec as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
import sys
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
    group_only = args.get("group_only" , False)
    private_only = args.get("private_only" , False)
    incoming = args.get("incoming" , False)
    outgoing = args.get("outgoing" , True)
    edited = args.get("edited" , True)
    
    def decorator(func):
        async def wrapper(event):
            if event.via_bot_id or event.fwd_from:
                return
            if groups_only and not event.is_group:
                return
            if private_only and not event.is_private:
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
            except BaseException as e:
                LOGS.info(e)
            date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            ftext += "**------- USERBOT LOGS ------**\n\n"
            ftext += f"**• Date:** ( `{date}` )\n"
            ftext += f"**• Chat ID:** ( `{event.chat_id}` )\n"
            ftext += f"**• Sender ID:** ( `{event.sender_id}` )\n\n"
            ftext += f"**• Event Trigger:**\n ( `{event.text}` )\n\n"
            ftext += f"**• Traceback Info:**\n ( `{str(format_exc())}` )\n\n"
            ftext += "**• Error Text:**\n ( `{str(sys.exc_info()[1])}` )"
            ftext += "\n\n\nLast 10 commits:\n"
            command = "git log --pretty=format:\"%an: %s\" -10"
            process = await asyncsubshell(command,
                                          stdout=asyncsub.PIPE,
                                          stderr=asyncsub.PIPE)
            stdout, stderr = await process.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())
            ftext += result
            file = open("Error.log", "w+")
            file.write(ftext)
            file.close()
            await event.edit("`• Sorry, My Userbot Has Crashed. The Error Logs Are Stored In The Userbot Log Chat!`")
            await event.client.send_file(LOG_GROUP, "Error.log", caption="**• Alien UserBot Logs!**")
            remove("Error.log")

        if edited:
            app.add_event_handler(wrapper, events.MessageEdited(**args))
        app.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper
    return decorator
