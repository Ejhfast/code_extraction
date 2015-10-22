# Return MongoEngine Documents as JSON
from bson import json_util
json_util.dumps(MyDoc._collection_obj.find(MyDoc.objects()._query))
