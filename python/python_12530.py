# fast update in mongo db
db.words.update({"_id": "the_word" }, {"$inc": {"frequency": 1}}, true)
