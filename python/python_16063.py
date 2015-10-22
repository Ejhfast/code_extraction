# Getting one Field prior to an atomic update in MongoEngine
DocA.objects(id=someid, user=logged_in_user).update_one(push__strings="New String")
