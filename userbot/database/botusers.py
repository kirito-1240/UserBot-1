from . import DB

def get_users():
    return DB.get_key("BOT_USERS") or {}

def add_user(user_id):
    if get_user(user_id) is False:
        users = get_users()
        users.update({"user_id": user_id})
        return DB.set_key("BOT_USERS", users)

def get_user(user_id):
    users = get_users()
    if users.get(user_id):
        return True
    return False
