# Selecting values from python dictionaries and string into new dicts
d = {1:23,2:20,3:10,4:9,5:1}
print({k:v for k,v in d.items() if v &gt;=10})
{1: 23, 2: 20, 3: 10}
