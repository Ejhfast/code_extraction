# python convert strings into sets of characters
c = ['a,b,c', 'a,b,c', 'a,b']
print (set (''.join (c).replace (',', '') ) )
