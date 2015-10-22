# Casting from list of lists of strings to list of lists of ints in python
x = [['565.0', '575.0'], ['1215.0', '245.0'], ['1740.0', '245.0']]
x = [[int(float(j)) for j in i] for i in x]
