# Is using __add__ in Python on an int a bad idea?
for i,tax in enumerate(othertaxes):
    basecost += tax.calculate(basecost,othertaxes[:i])
