from pymongo import MongoClient


client = MongoClient()
db = client['employee']

empinfo = db['empinfo']

def sanitize_op(doc):
    del doc["_id"]

def getallempdata():
    data = list(empinfo.find({}))
    for info in data:
        sanitize_op(info)

    return data

def getempid(name):
    data = empinfo.find_one({"name": name})
    id = None
    if data is not None:
        id = data['id']

    return id

def getempdata(empid):
    data = empinfo.find_one({"id": empid})
    
    if data is not None:
        sanitize_op(data)

    print(data)
    return data


def updatedesc(empid, desc):
    empinfo.update_one(
        { "id":empid },
        {
            "$set": {
                "desc": desc
            }
        }
    )


