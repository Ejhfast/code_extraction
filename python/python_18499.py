# Python replace indentation with period
rhs = data.lstrip()
print '.' * (len(data) - len(rhs)) + rhs
