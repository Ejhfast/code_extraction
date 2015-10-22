# filter string in comprehension list with nested loops
s = 'ab, c d'
cmpfn = lambda x: -len(x)
sorted([''.join(y for y in x if y.isalnum()) for x in s.split()], key=cmpfn)[0]
