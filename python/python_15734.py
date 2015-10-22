# Check if datastore is empty
exists = Map.all().count(limit=1)
if exists: # it's not empty!
