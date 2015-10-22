# python: Searching strings in one list in another list, then appending an entire list entry to a new list
s = set(L1)
new_list = [a for a in L2 if any(b in s for b in a)]
