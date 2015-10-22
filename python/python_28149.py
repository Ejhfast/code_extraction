# Generate a random array ignoring a selected value
first_value = random.randint(0, 10)
randarray = [i for i in random.sample(range(0, 10), 10) if i != first_value]
randarray.insert(0, first_value)
