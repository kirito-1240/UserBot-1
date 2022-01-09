from userbot import app
from telethon import events
import os
from userbot.utils import runcmd
os.system("pip install deep_translator")
from deep_translator import GoogleTranslator

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.tr (.*)$"))
async def Translator(event):
    edit = await event.edit("`Please Wait ...`")
    lang = str(event.text[3:])
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.media and reply.document.mime_type == "text/plain" and not reply.text:
        media = reply.media
        await app.download_media(media , "input.txt")
        file = open("input.txt")
        text = file.read()
        output = GoogleTranslator(source='auto', target=lang).translate(text)
        os.remove("input.txt")
        if len(str(output)) < 4000:
            await edit.edit(f"""**• Your Text:** \n( `{text}` )\n\n**• Translate To** `{lang}`:\n ( `{output}` )""")
        else:
            with open('Result.txt', 'w') as f:
                f.write(f"""**• Your Text:** \n( `{text}` )\n\n**• Translate To** `{lang}`:\n ( `{output}` )""")
                f.close()
            await edit.delete()
            await app.send_file(event.chat_id, "Result.txt" , caption="**• See The Answer In The File!**" , reply_to=reply.id)
            os.remove("Result.txt")
    elif not event.reply_to == None and reply.text:
        text = reply.text
        output = GoogleTranslator(source='auto', target=lang).translate_file(text)
        if len(str(output)) < 4000:
            await edit.edit(f"""**• Your Text:** \n( `{text}` )\n\n**• Translate To** `{lang}`:\n ( `{output}` )""")
        else:
            with open('Result.txt', 'w') as f:
                f.write(f"""**• Your Text:** \n( `{text}` )\n\n**• Translate To** `{lang}`:\n ( `{output}` )""")
                f.close()
            await edit.delete()
            await app.send_file(event.chat_id, "Result.txt" , caption="**• See The Answer In The File!**" , reply_to=reply.id)
            os.remove("Result.txt")
    else:
        await edit.edit("**• Please Reply To File Or Message For Translate!**")     
