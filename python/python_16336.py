# How to 'pickle' an object to a certain directory?
with open('/full/path/to/file', 'wb') as f:
    pickle.dump(object, f)
