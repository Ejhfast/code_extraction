# Getting lists where an element passes through every index in python?
l = [1,2,3]
new_l = [l[:i] + [9] + l[i:] for i in range(len(l) + 1)]
