# Find all the strings with max length using max() function
maxlen = len(max(l, key=len))
maxlist = [s for s in l if len(s) == maxlen]
