# Replacing Nones in a python array with zeroes
allorders = [i if i[0] is not None else (0, i[1]) for i in allorders]
