# How use sql "like" in PyMongo?
db.houses.find({"hid":{"$regex": u"9"}})
