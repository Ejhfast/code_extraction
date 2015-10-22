# MongoDB object pointing
for doc in coll.find():      # .find() returns cursor which is meant for iteration
    print(doc["oxigeno"])    # doc is a python dictionary representing the returned BSON document
