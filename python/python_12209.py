# How do I prevent application calling datastore_v3.next() when calling get_multi?
keys = [k.parent() for k in result_keys]
