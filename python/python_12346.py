# MongoDB and Twitter query
cursor = coll.find({ $or : [{"coordinates.type" : "Point"},{"location": {$ne :"null" }}]},{"coordinates" :1}, tailable = True, timeout = False)
