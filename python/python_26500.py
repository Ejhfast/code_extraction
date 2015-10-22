# mongoengine user with readWrite can not create indexes
db = connect("magic", "alias", host="my.url.com", port=port)
db["magic"].authenticate("user", password="pwd")
