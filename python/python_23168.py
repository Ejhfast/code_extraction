# mongodb, pymongo - sort matching data by another column
db.location.find({'location':{$regex:'blah'}}).sort({'country':-1}).limit(20)
