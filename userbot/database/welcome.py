from userbot.database import DB

def get_chats():
    return DB.get_key("WELCOME_CHATS") or {}

def set_welcome(chat_id , message , media , entity):
    chats = get_chats()
    if not get_welcome(chat_id):
        chats.update({chat_id: {"message": message , "media": media , "entities": entity}})
        return DB.set_key("WELCOME_CHATS", chats)
    else:
        DB.del_key(chats[chat_id])
        chats.update({chat_id: {"message": message , "media": media , "entities": entity}})
        return DB.set_key("WELCOME_CHATS", chats)

def get_welcome(chat_id):
    chats = get_chats()
    try:
        return chats[chat_id]
    except:
        return None

def del_welcome(chat_id):
    chats = get_chats()
    if get_welcome(chat_id):
        del chats[chat_id]
        return DB.set_key("WELCOME_CHATS", chats)
