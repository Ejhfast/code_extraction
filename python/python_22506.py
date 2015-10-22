# Python: Verifying a prime number
def is_prime(a):
    return all(a % i for i in xrange(2, a))
