# Serialize a Python dict into a Cassandra 1.2 column
obj_to_store = cPickle.dumps(input_obj).encode("hex")
