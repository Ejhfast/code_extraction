# How to compute sum of squares of two largest numbers out of three in python
def two_of_three(a,b,c):
    return a**2+b**2+c**2-min([a,b,c])**2
