# Count lower case characters in a string
def n_lower_chars(string):
    return sum(1 for c in string if c.islower())
