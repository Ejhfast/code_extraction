# How to subtract values from dictionaries
d3 = {key: d1[key] - d2.get(key, 0) for key in d1.keys()}
