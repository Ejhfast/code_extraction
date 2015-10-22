# how to query an element from a list in pymongo
list(db.users.find({"document_up.tags":{"$in":["solide"]}}))
