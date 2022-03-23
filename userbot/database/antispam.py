from . import DB

def get_limit():
    return DB.get_key("ANTI_SPAM_LIMIT") or None

def set_limit(lim):
    DB.set_key("ANTI_SPAM_LIMIT" , lim)

def get_power():
    return DB.get_key("ANTI_SPAM_POWER") or "off"

def set_power(pow):
    DB.set_key("ANTI_SPAM_POWER" , pow)

def get_users():
    return DB.get_key("ANTI_SPAM_USERS") or {}

def add_user(user_id):
    users = get_users()
    count = int(get_user(user_id)) + 1
    users.update({user_id: count})
    return DB.set_key("ANTI_SPAM_USERS", users)

def get_user(user_id):
    users = get_users()
    try:
        return users[user_id]
    except:
        return 0

def del_user(user_id):
    users = get_users()
    if get_user(user_id):
        del users[user_id]
        return DB.set_key("ANTI_SPAM_USERS", users)
    else:
        return False
