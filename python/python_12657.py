# How to convert a list of string to a list of int
a = [['1','2','3','4'],['1','2','3','4'],['1','2','3','4']]
b = [ [int(j) for j in i] for i in a]
