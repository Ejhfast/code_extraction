# How to make a function that counts how many times each element is equal to 2 elements to its right
s = "evening"
ans = len([x for x in xrange(len(s)-2) if s[x] == s[x+2]])
print ans
