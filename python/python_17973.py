# Generating random values in python
both = [ random.randint(0, 500) for i in range(100) ]
odd = [ x for x in both if x % 2 == 1 ]
even = [ x for x in both if x % 2 == 0 ]
