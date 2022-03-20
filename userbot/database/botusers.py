from userbot.db import set_key , get_key

def add_user(id):
    users = get_key("BOT_USERS")
    if not id in users:
        users.append(id)
        set_key("BOT_USERS", users)

def users_count():
    return len(get_key("BOT_USERS"))
