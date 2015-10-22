# How to check if number is integer number, with good precision?
def is_square(x):
    s = int(sqrt(x) + 0.5)
    return s * s == x
