# Repeated Random Numbers
numbers = list(range(1, 101)) # all the numbers in the bag, from 1 to 100
random.shuffle(numbers)       # shake the bag
bingo_num = numbers.pop()     # pull out next number (inside your loop)
