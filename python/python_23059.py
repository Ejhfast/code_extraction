# mongoengine unique constraing
db = new Mongo().getDB("mirad");
 db.source_model.dropIndex("name_1")
