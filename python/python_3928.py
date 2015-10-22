# Removing a character in a string one at a time
In [6]: s = "abaccea"
In [9]: [s[:key] + s[key+1:] for key,val in enumerate(s) if val == "a"]
Out[10]: ['baccea', 'abccea', 'abacce']
