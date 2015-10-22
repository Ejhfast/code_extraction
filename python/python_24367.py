# How can I make a code that determines if a list is sorted or not in Python?
def is_sorted(lst):
    return all(a &lt;= b for a,b in zip(lst, lst[1:]))
