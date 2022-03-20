from userbot.database import set_key , get_key , del_key , keys

def add_user(id):
    users = get_key("BOT_USERS")
    if not id in users:
        users.append(id)
        set_key("BOT_USERS", users)
