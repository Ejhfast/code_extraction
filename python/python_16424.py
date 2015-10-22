# Python: comprehension to compose two dictionaries
result = {k: d2.get(v) for k, v in d1.items()}
