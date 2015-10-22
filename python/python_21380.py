# Implementing ensureIndex() to delete duplicate documents with pymongo
db.collection.ensure_index([("x" , pymongo.ASCENDING), ("unique" , True), ("dropDups" , True)])
