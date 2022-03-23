from . import DB

def get_chats():
    return DB.get_key("WELCOME_CHATS") or {}

def set_welcome(chat_id , msg):
    chats = get_chats()
    if chat_id not in chats.keys():
        chats.update({chat_id: msg})
        return DB.set_key("WELCOME_CHATS", chats)
    else:
        del chats[chat_id]
        chats.update({chat_id: msg})
        return udB.set_key("WELCOME_CHATS", chats)

def get_welcome(chat_id):
    chats = get_chats()
    if chat_id in chats.keys():
        return chats[chat_id]


def del_welcome(chat_id):
    chats = get_chats()
    if chat_id in chats.keys():
        del chats[chat_id]
        return udB.set_key("ANTIFLOOD", chats)
