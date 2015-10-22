# appengine: cached reference property?
keys = [MyModel.ref.get_value_for_datastore(x) for x in referers]
referees = db.get(keys)
