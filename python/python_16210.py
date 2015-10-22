# summation of 1000 different random numbers between 80-130?
import random
sum(random.random()*50 + 80 for _ in range(1000))
