from . import DB

def get_users():
    return DB.get_key("ECHO_USERS") or []

def add_user(user_id):
    users = get_users()
    if not users:
        if user_id not in users:
            return DB.set_key("ECHO_USERS", [user_id])
    else:
        if user_id not in users:
            users.append(user_id)
            return DB.set_key("ECHO_USERS", users)  

def del_user(user_id):
    users = get_users()
    if user_id in users:
        return DB.del_key("ECHO_USERS", user_id)
    else:
        return False
