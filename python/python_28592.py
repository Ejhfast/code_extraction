# Does python store one value for an int and many references?
interned_range = [i for i in range(-1000, 1000) if i+0 is i]
print min(interned_range), max(interned_range)
