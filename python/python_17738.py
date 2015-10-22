# Given a subset of attributes on a class instance, increment one randomly
attributes = ['pandas', 'tunas', 'cows']
choice = random.choice(attributes)
setattr(z, choice, getattr(z, choice) + 1)
