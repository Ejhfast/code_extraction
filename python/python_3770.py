# Changing python immutable type while iterating through a mutable container such as list
strings = ['a', 'b']
strings = [s + 'c' for s in strings]
