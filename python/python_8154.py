# Python 3: Generate not all permutations, but all non-repetitive combinations of length r?
("".join(s) for s in product(alphabet, repeat=n) if s[:n//2]!=s[n//2:])
