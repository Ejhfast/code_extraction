# search by ObjectId in mongodb with pymongo
from bson.objectid import ObjectId
[i for i in dbm.neo_nodes.find({"_id": ObjectId(obj_id_to_find)})]
