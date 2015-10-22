# Python's example for "iter" function gives me TypeError
with open("mydata.txt") as fp:
    for line in iter(fp.readline, ''):
        print line
