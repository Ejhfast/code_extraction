# How to Convert a Text File into a List in Python
crimefile = open(fileName, 'r')
yourResult = [line.split(',') for line in crimefile.readlines()]
