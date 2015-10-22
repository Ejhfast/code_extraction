# How do I trim the number of words in Python?
def f(s, n):
    return ' '.join(s.split()[:n])
