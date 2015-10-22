# Cannot filter a non-Node argument - datastore - google app engine - python
x = userData.query().filter(ndb.GenericProperty("age") &gt;= 1).get()
