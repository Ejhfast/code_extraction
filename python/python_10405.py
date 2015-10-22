# What's the best way to parse values from a variable length string?
a, b, c = 10, 10, 1    #default values
mylist = [int(x) for x in input.split(',')]
a, b, c = mylist + [a, b, c][len(mylist):]
