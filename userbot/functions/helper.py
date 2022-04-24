import string, random

def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None

def rand_string(count):
    strings = (string.ascii_letters + str(string.digits))
    text = ""
    for x in range(0, int(count)):
        text += random.choice(strings)
    return text
