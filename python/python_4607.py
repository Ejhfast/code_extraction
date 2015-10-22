# Inserting new attribute to a document using MongoDB ( Python )
db.collection.update({'_id' : ObjectId(...)},
                     {'$set' : {'create_time' : datetime(..) }})
