# python- with an undetermined tuple (str), how to find if a letter is in each one of the strings
def func(*args):
    return all('a' in str(x) for x in args)
