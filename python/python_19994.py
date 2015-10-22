# Prepend line number to string in python
f = open('workfile', 'r')
for num,line in enumerate(f):
    print(num+" "+line)
