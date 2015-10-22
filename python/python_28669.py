# Python Recursion - Finding sum of max and min in a nested array
def find_max(my_list):
    m = max([find_max(x) if type(x) is list else x for x in my_list])
    return m
