from . import DB

def get_chats():
    return DB.get_key("FCOM_CHATS") or {}

def add_fcom(chat_id, msg_id):
    chats = get_chats()
    if not get_fcom(chat_id):
        chats.update({chat_id: msg_id})
        return DB.set_key("FCOM_CHATS", chats)
    else:
        DB.del_key(chats[chat_id])
        chats.update({chat_id: msg_id})
        return DB.set_key("FCOM_CHATS", chats)

def get_fcom(chat_id):
    chats = get_chats()
    try:
        return chats[chat_id]
    except:
        return None

def del_fcom(chat_id):
    chats = get_chats()
    if get_fcom(chat_id):
        del chats[chat_id]
        return DB.set_key("FCOM_CHATS", chats)
    else:
        return False

def clean_fcoms():
    DB.del_key("FCOM_CHATS")
