# How do I generate a random string (of length X, a-z only) in Python?
''.join(random.choice(string.lowercase) for x in range(X))
