# File opened in a function doesn't need to be closed manually?
with open(f_name) as f:
    # do stuff with f
    # possibly throw an exception
