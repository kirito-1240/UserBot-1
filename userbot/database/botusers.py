from sqlalchemy import Column, String, UnicodeText

from . import BASE, SESSION

class Bot_Users(BASE):
    __tablename__ = "BOT_USERS"
    user_id = Column(String(14), primary_key=True)
    date = Column(UnicodeText)
    def __init__(self , user_id , date):
        self.user_id = str(user_id)
        self.date = date

Bot_Users.__table__.create(checkfirst=True)

def add_user(user_id , date):
    to_check = info_user(user_id)
    if not to_check:
        user = Bot_Users(str(user_id) , date)
        SESSION.add(user)
        SESSION.commit()
        return True
    rem = SESSION.query(Bot_Users).get(str(user_id))
    SESSION.delete(rem)
    SESSION.commit()
    user = Bot_Users(str(user_id) , date)
    SESSION.add(user)
    SESSION.commit()
    return True

def info_user(user_id):
    try:
        _result = SESSION.query(Bot_Users).get(str(user_id))
        if _result:
            return _result
        return None
    finally:
        SESSION.close()

def get_users():
    try:
        return SESSION.query(Bot_Users).all()
    except BaseException:
        return None
    finally:
        SESSION.close()
