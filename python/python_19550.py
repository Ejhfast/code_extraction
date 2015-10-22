# How to unpack optional items from a tuple?
foo, bar, baz == (list(a) + [None]*3)[:3]
