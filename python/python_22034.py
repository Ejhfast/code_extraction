# Add a list to an already stored document in pymongo
collection.update({ "_id" : id },{"$set": {"list_followers": ids}})
