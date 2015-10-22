# Best way to eliminate duplicates in a list, but keep previous relative order
seen = set()
item_list = [seen.add(item) or item for item in item_list if item not in seen]
