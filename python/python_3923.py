# How do I update a Mongo document after inserting it?
mycollection.update({'_id':mongo_id}, {"$set": post}, upsert=False)
