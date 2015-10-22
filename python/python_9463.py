# Python List Comprehensions Splitting loop variable
[(x[1],x[2]) for x in (x.split(";") for x in a.split("\n")) if x[1] != 5]
