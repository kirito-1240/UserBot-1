from . import DB

db = DB["BOT_USERS"]

async def add_user(user_id):
    if check_user(user_id) is False:
        await db.insert_one({"user_id": user_id})

async def check_user(user_id):
    Lol = await db.find_one({"user_id": user_id})
    return bool(Lol)

async def get_all_users():
    return db.find()
