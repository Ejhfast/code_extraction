# nested queries in pymongo using collection.find()
db.test_collection.find({"data.Country": "ES"})
db.test_collection.find({"data.Count": {"$lt": 6}})
