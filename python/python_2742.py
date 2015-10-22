# How to get sorted results in MongoKit?
db.articles.find().sort({_id: -1}).limit(10);
