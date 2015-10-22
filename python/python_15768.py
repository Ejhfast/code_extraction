# Mutating list in python
def initialize_one(seq, n):
    if not seq:
        seq[:] = [1] * n
