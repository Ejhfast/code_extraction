# Running timeit in a for loop with index as input number
for i in range(1, 30):
    t = timeit.Timer('Fib({:d})'.format(i), 'from problem1 import Fib').timeit()
    print('The time for {i:d} is {t:0.2f}'.format(i=i, t=t))
