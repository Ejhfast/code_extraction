# haskell's "where" in python's list comprehensions
[dif for dif in (lst[i]-lst[i-1] for i in range(1, len(lst))) if dif &lt; 5]
