# Is there a simple way to create a hash of list of dictionaries?
hashlib.md5(pickle.dumps(a[0])).hexdigest()
