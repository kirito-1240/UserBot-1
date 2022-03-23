from . import DB
import json

def get_chats():
    return DB.get_key("WELCOME_CHATS") or {}

def set_welcome(chat_id , msg):
    chats = json.loads(get_chats())
    if not get_welcome(chat_id):
        chats.update({chat_id: msg})
        return DB.set_key("WELCOME_CHATS", chats)
    else:
        del chats[chat_id]
        chats.update({chat_id: msg})
        return udB.set_key("WELCOME_CHATS", chats)

def get_welcome(chat_id):
    chats = json.loads(get_chats())
    try:
        return chats[chat_id]
    except:
        return None

def del_welcome(chat_id):
    chats = json.loads(get_chats())
    if get_welcome(chat_id):
        del chats[chat_id]
        return udB.set_key("WELCOME_CHATS", chats)
