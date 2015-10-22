# pythonic way of selecing a random value that satisfies a certain predicate
intlist = range(1,10)
randomeven = random.choice([i for i in intlist if i % 2 == 0])
