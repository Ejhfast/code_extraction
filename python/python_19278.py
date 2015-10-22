# How to solve TypeError: spec must be an instance of dict on pymongo
posts4 = db4.posts
post_id4 = posts4.update({'id' : usr.get('id')}, dict4, upsert = True)
