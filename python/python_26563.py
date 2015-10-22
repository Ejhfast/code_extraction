# Get data of Referenced objects in MongoEngine query, not just id
posts = mongo.ListField(mongo.ReferenceField(Post, dbref=True))
