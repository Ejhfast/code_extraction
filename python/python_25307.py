# NDB Model Querying of Key Ids using an array filter
keys = [ndb.Key(MyModel, anid) for anid in ids]
objs = ndb.get_multi(keys)
