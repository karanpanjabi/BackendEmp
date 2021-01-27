from pymongo import MongoClient
import json

client = MongoClient()
db = client['employee']

empinfo = db['empinfo']

coll_data = None

with open("data.json") as f:
    coll_data = json.load(f)

empinfo.delete_many({})
empinfo.insert_many(coll_data)