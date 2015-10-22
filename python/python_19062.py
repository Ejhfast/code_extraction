# Assign multiple values in range
for v,c in zip([1, 2, 3, 4], ws['A1':'D1']):
     c.value = v
