# How do I get all the keys that are stored in the Cassandra column family with pycassa?
list(cf.get_range().get_keys())
