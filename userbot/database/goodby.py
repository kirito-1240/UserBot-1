from userbot.database import DB

def get_chats():
    return DB.get_key("GOODBY_CHATS") or {}

def add_goodby(chat_id, msg_id):
    chats = get_chats()
    if not get_goodby(chat_id):
        chats.update({chat_id: msg_id})
        return DB.set_key("GOODBY_CHATS", chats)
    else:
        DB.del_key(chats[chat_id])
        chats.update({chat_id: msg_id})
        return DB.set_key("GOODBY_CHATS", chats)

def get_goodby(chat_id):
    chats = get_chats()
    try:
        return chats[chat_id]
    except:
        return None

def del_goodby(chat_id):
    chats = get_chats()
    if get_goodby(chat_id):
        del chats[chat_id]
        return DB.set_key("GOODBY_CHATS", chats)
    else:
        return False

def clean_goodbys():
    DB.del_key("GOODBY_CHATS")
