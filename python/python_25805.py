# How to divide a 2D list into one 2D list and one array (remove the last column)
sublist = [[a[0], a[1]] for a in list]
subarray = [a[2] for a in list]
