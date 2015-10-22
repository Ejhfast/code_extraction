# Sort a dictionary by length of the value
sorted_items = sorted(d.items(), key = lambda item : len(item[1]))
newd = dict(sorted_items[-2:])
