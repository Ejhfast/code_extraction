# select rows in appengine database based on key ids
item = db.get(db.Key.from_path('Notes', id))
