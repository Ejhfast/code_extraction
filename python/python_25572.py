# Pandas apply to dateframe produces '<built-in method values of ...'
temp = zip(list(data.geom), list(data.address))
output = map(lambda x: {'geometry': x[0], 'properties':{'address':x[1]}}, temp)
