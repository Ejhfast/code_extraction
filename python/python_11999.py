# How to add +1 to every nth number in list, python
for i in xrange(0, len(list)):
    if i % 2 == 0:
        list[i] += 1
