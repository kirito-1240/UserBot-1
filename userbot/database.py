import os
import sys
os.system("pip install pymongo")
from pymongo import MongoClient

class MongoDB:

    def __init__(mongo_url):
        DBClient = MongoClient(mongo_url)
        DB = DBClient["UserBot"]

    def keys(self):
        return DB.list_collection_names()

    def set_key(key , value):
        if key in keys():
            DB[key].replace_one({key: value})
        else:
            DB[key].insert_one({key: value})

    def del_key(key):
        if key in keys():
            DB.drop_collection(key)
            
    def get_key(key):
        if key in keys():
            value = DB[key].find_one(key)
            return value
