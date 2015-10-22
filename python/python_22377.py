# unable to query Mongodb using pymongo
query = db.fyp.find({ userInputFirst : {'$regex':userInputSecond, '$options' : 'i'}})
