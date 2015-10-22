# Sort a dictionary according to the lists size and then alphabetically by their key in Python?
D = [ (x, Dict[x]) for x in Dict]
ascending = sorted(D, key = lambda x: x[1])
ascending.sort()
