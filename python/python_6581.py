# python remove duplicate dictionaries from a list
result = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in l)]
