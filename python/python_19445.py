# Python challenge: distinct combination of prime numbers in a given range
def nPk(n,k):
    return int( factorial(n)/(factorial(n- k) * factorial(k)))
