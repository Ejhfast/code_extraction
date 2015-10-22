# Python GAE datastoreAttributeError: 'NoneType' object has no attribute
first_query = db.GqlQuery("SELECT * FROM Contract ORDER BY date DESC").get()
