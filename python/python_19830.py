# How can I make the default value of an argument depend on another argument (in Python)?
def func(n=5.0, delta=None):
     if delta is None:
         delta = n/10
