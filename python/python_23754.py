# List of lists of objects to JSON with Python
json.dumps([[ob.__dict__ for ob in lst] for lst in list_dep])
