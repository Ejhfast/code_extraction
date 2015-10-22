# Remove items from list of dicts with a matching attribute
data = [d for d in data if d['id'] not in remove_ids]
