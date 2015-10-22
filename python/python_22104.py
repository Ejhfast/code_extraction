# Check if a list is not empty pymongo
collection.find({'list_followers': {'$not': {'$size': 0}}}))
