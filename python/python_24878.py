# Find all keys with the max same value in python
maxv = max(b.values())
new_list = [k for k, v in b.items() if v == maxv]
