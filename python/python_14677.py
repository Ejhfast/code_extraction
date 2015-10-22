# How to readjust defaultdict(list)s - Python
{(k1,v):k2 for k1 in dict1 for k2 in dict2
           for v in dict2[k2] if k2 in dict1[k1]}
