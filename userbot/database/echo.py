from . import DB

def get_chats():
    return DB.get_key("ECHO_USERS") or {}

def add_echo(chat_id, user_id):
    chats = get_chats()
    if not get_echo(chat_id):
        chats.update({chat_id: user_id})
        return DB.set_key("ECHO_USERS", chats)

def get_echo(chat_id):
    chats = get_chats()
    try:
        return chats[chat_id]
    except:
        return None

def del_echo(chat_id):
    chats = get_chats()
    if get_echo(chat_id):
        del chats[chat_id]
        return DB.set_key("ECHO_USERS", chats)
    else:
        return False

def clean_echos():
    DB.del_key("ECHO_USERS")
