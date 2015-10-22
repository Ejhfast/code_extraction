# Common characters within strings in 2 lists in Python
c = [item for item in a
     if any(name in item for name in b)]
