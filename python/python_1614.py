# Adding a string in front of a string for each item in a list in python
n = [i if i.startswith('h') else 'http' + i for i in n]
