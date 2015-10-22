# Construct String based off length of list
'{%s}' % ','.join('(%s)' % element for element in x)
