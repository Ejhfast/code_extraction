# Getting multiple entities with get_by_id in ndb
objects = ndb.get_multi([ndb.Key(Model, k) for k in ids])
