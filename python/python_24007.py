# Replace substrings with elements of a list of tuples
newstring = string
for a,b in t:
    newstring = newstring.replace(a,b)
