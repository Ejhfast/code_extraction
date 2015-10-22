# Python switch order of elements
s="abcdefgh"
print "".join(b+a for a,b in zip(s[::2],s[1::2]))
