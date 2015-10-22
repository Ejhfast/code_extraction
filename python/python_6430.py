# Is list comprehension appropriate here?
l.extend((i for i in (2,3,4) if i not in l))
