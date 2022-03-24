from . import DB

def get_users():
    return DB.get_key("ECHO_USERS") or []

def add_user(user_id):
    users = get_users()
    if str(type(users)) == "<class 'list'>":
        if user_id not in users:
            users.append(user_id)
            return DB.set_key("ECHO_USERS", users)
    else:
        users = [get_users()]
        if user_id not in users:
            users.append(user_id)
            return DB.set_key("ECHO_USERS", users)
            
def get_user(user_id):
    users = get_users()
    if user_id in users:
        return True
    else:
        return False

def del_user(user_id):
    users = get_users()
    if get_user(user_id):
        del users[user_id]
        return DB.set_key("ANTI_SPAM_USERS", users)
    else:
        return False
