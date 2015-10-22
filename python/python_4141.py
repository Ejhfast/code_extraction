# Serializing ReferenceProperty in Appengine Datastore to JSON
cwt = commonWordTweets()   # Replace with code to get the item from your datastore
d = {"commonWords":cwt.commonWords, "venue": cwt.venue.name}
jsonout = simplejson.dumps(d)
