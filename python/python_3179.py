# Lowest common multiple for all pairs in a list
def lcm(numbers):
    return map(__lcm, combinations( numbers, 2 ) )
