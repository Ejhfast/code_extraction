# Why mutable not working when expression is changed in python ?
y += [1,3]   # Means append to y list [1,3], object stays same
y = y+[1,3]  # Means create new list equals y + [1,3] and write link to it in y
