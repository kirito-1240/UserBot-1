from . import DB

db = DB["BOT_USERS"]

def add_user(user_id):
    if check_user(user_id) is False:
        db.insert_one({"user_id": user_id})

def check_user(user_id):
    Lol = db.find_one({"user_id": user_id})
    return bool(Lol)

def get_all_users():
    return [s for s in db.find()]
