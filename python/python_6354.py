# How can I make array B from array A without infinities included in Python 2.7?
B = filter(lambda x: abs(x) != float('inf'), A)
