# MongoDB group with multiple id
db.collection.aggregate([ { $match: { "type" : { "$exists" : true}, "location" : { "$exists" : true}, "language" : { "$exists" : true}} } ])
