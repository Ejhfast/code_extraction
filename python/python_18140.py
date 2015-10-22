# Why do list comprehensions write to the loop variable, but generators don't?
x = 'before'
a = [x for x in 1, 2, 3]
print x # this prints '3', not 'before'
