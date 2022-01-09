from userbot import app
from telethon import events
import os
from userbot.utils import runcmd
os.system("pip install deep_translator")
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException , NotValidLength

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.tr (.*)$"))
async def Translator(event):
    await event.edit("`• Please Wait ...`")
    lang = str(event.text[4:])
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.media and reply.document.mime_type == "text/plain" and not reply.text:
        media = reply.media
        await app.download_media(media , "input.txt")
        file = open("input.txt")
        text = file.read()
        try:
            output = GoogleTranslator(source='auto', target=lang).translate(text)
        except LanguageNotSupportedException:
            return await event.edit("**• Language Not Supported!**")
        except NotValidLength:
            return await event.edit("**• Not Valid Text Length!**")
        os.remove("input.txt")
        if len(str(output)) < 4000:
            await event.edit(f"""**• Your Text:** \n{text}\n\n**• Translate To {lang}**:\n {output}""")
        else:
            with open('Result.txt', 'w') as f:
                f.write(f"""• Your Text: \n{text}\n\n• Translate To {lang}:\n {output}""")
                f.close()
            await event.delete()
            await app.send_file(event.chat_id, "Result.txt" , caption="**• See The Answer In The File!**" , reply_to=reply.id)
            os.remove("Result.txt")
    elif not event.reply_to == None and reply.text:
        text = reply.text
        try:
            output = GoogleTranslator(source='auto', target=lang).translate(text)
        except LanguageNotSupportedException:
            return await event.edit("**• Language Not Supported!**")
        except NotValidLength:
            return await event.edit("**• Not Valid Text Length!**")
        if len(str(output)) < 4000:
            await event.edit(f"""**• Your Text:** \n{text}\n\n**• Translate To {lang}**:\n {output}""")
        else:
            with open('Result.txt', 'w') as f:
                f.write(f"""• Your Text: \n{text}\n\n• Translate To {lang}:\n {output}""")
                f.close()
            await event.delete()
            await app.send_file(event.chat_id, "Result.txt" , caption="**• See The Answer In The File!**" , reply_to=reply.id)
            os.remove("Result.txt")
    else:
        await event.edit("**• Please Reply To File Or Message For Translate!**")     
