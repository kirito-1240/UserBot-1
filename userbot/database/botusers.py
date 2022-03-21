from userbot.db import set_key , get_key

def get_all_users(key):
    return get_key(key) or []

def is_added(id):
    return id in get_all_users("BOT_USERS")

def add_user(id):
    users = get_all_users("BOT_USERS")
    if not is_added(id):
        users.append(id)
        return set_key("BOT_USERS", users):
    
def users_count():
    return len(get_key("BOT_USERS"))
