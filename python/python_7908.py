# In Python, how do I count the trailing zeros in a string or integer?
def trailing_zeros(longint):
    manipulandum = str(longint)
    return len(manipulandum)-len(manipulandum.rstrip('0'))
