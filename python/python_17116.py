# Sorting with a python dictionary
l = documents.items()
l.sort(key=lambda x: x[1]['weight'], reverse=True)
result = [d[0] for d in l]
