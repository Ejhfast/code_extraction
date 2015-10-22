# Pythonic random list of booleans of length n with exactly k Trues
output = sorted([1] * k + [0] * (n - k), key=lambda k: random.random())
