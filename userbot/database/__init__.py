import os
os.system("pip install pymongo[srv]")
from pymongo import MongoClient

cl = MongoClient(
             "mongodb+srv://userbot:abol83@userbot.smv0r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
              username="userbot",
              password="abol83"
         )

DB = cl["UserBot"]
