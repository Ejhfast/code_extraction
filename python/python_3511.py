# Create a new variable as named from input in Python?
g = globals() # get a reference to the globals dict
g[raw_input("Name Please")] = raw_input("Value Please")
print foo
