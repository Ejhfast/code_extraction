# Generate 20 random integers and indicate whether each number is odd or even
import random
print('\n'.join("%s is %s"%(i_got_this_from_stackoverflow, "odd" if i_got_this_from_stackoverflow%2 else "even")for i_got_this_from_stackoverflow in random.sample(list(range(int(input("Please enter the lower bound of the numbers: ")), int(input("Please enter the upper bound of the numbers: ")))), 20)))
