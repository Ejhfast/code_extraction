# Comparing items within a list with each other
new = [(i, i - 1) for i in lst if i - 1 in lst]
