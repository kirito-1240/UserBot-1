import os
os.system("pip install pymongo[srv]")
from pymongo import MongoClient
from Config import Config

client = MongoClient(Config.MongoDB_URL , serverSelectionTimeoutMS=5000)

DB = client["UserBot"]
