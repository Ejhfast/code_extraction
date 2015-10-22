# Retrieve key from automatically assigned ID which has been passed through URL in GAE, using ndb and python
this_key = ndb.Key(urlsafe=resource)
query_result_as_entity = this_key.get()
