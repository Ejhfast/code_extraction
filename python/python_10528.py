# How to generate exponentially increasing range in Python
numbers_sizes = (i*10**exp for exp in range(2, 9) for i in range(1, 10))
for n in numbers_sizes:
    test(n)
