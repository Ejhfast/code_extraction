# Find the number of digits in the fractional part of a Decimal number in python
def digits(n):
    return max(0,-n.as_tuple().exponent)
