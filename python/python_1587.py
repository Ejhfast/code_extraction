# Reverse loop inside a loop with same list
for n1, n2 in izip(num, reversed(num)):
    print n1, '\t', n2
