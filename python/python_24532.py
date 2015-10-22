# Pymongo using $exists
collection.find({"$and":[ {"cwc":{"$exists": True}}, {"cwc":{"$ne": ""}}]})
