# MongoDB/py-mongo for queries with date functions
db.foo.find({"purchase_date": {"$gt": monday_midnight, "$lte": tuesday_midnight}})
