from . import DB

def get_users():
    return DB.get_key("BOT_USERS") or []

def add_user(user_id):
    users = get_users()
    if get_user(user_id) is True:
        users.append(str(user_id))
        return DB.set_key("BOT_USERS", users)

def get_user(user_id):
    users = get_users()
    if user_id in users:
        return True
    return False
