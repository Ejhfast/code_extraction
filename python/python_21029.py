# Convert multidimensional array dimension in Python
[item if isinstance(item, list) else [item] for items in data for item in items]
# [[0], [1], [2], [3], [4], [5], [6, 9], [7], [8], [6, 9]]
