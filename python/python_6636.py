# Pymongo auto sort the input dictionary
mongo_keys = ["location.coords", "name"]
for k in mongo_keys:
    do_something(mongo_result[k])
