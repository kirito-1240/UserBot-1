from . import DB

def get_users():
    return [DB.get_key("BOT_USERS")]

def add_user(user_id):
    users = get_users()
    if user_id not in users:
        users.append(user_id)
        return DB.set_key("BOT_USERS", users)
