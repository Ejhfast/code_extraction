# How do I filter out non-string keys in a dictionary in Python?
{ key: dict[key] for key in dict.keys() if isinstance(key, int) }
