from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["instadb"]
collection = db["users"]

user= {"name": "pavan"}