# how to query using isodate in pymongo
test_range = agents.coll.find({ "created_at": {"$gte" : datetime(2015, 3, 1), "$lt": datetime(2015, 3, 30)}})
