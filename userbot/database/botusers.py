from sqlalchemy import Column, String, UnicodeText

from . import BASE, SESSION

class Bot_Users(BASE):
    __tablename__ = "BOT_USERS"
    user_id = Column(String(14), primary_key=True)
    def __init__(self , user_id , date):
        self.user_id = str(user_id)

Bot_Users.__table__.create(checkfirst=True)

def add_user(user_id):
    if not get_user(user_id):
        user = Bot_Users(str(user_id))
        SESSION.add(user)
        SESSION.commit()

def get_user(user_id):
    try:
        result = SESSION.query(Bot_Users).get(str(user_id))
        if result:
            return True
        return False
    finally:
        SESSION.close()

def get_users():
    try:
        return SESSION.query(Bot_Users).all()
    except BaseException:
        return None
    finally:
        SESSION.close()
