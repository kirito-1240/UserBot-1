import os , sys
from Config import Config
os.system("pip install pymongo[srv]")
from pymongo import MongoClient

DBClient = MongoClient(Config.MongoDB_URL)
DB = DBClient["UserBot"]
    
def get_keys():
    return DB.list_collection_names()

def set_key(key , value):
    if key in get_keys():
        DB[key].replace_one({key: value})
    else:
        DB[key].insert_one({key: value})

def del_key(key):
    if key in get_keys():
        DB.drop_collection(key)
            
def get_key(key):
    if key in get_keys():
        value = DB[key].find_one(key)
        return value
