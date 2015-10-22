# python + pymongo: how to insert a new field on an existing document in mongo from a for loop
db.Doc.update({"_id": b["_id"]}, {"$set": {"geolocCountry": myGeolocCountry}})
