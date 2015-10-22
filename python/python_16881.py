# How to use multiple random strings in Python / Pyramid?
import random
errors = ['dog ate it', 'flying monkeys stole it', 'rabbits attacked it']
value = {'result': 'error', 'message': random.choice(errors)}
