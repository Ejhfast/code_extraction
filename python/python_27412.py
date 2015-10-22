# MongoDB: How to determine is specific value does not exist
db.collection.find({"actions.action_type": {"$ne": "History"}})
