# Python list comprehension rebind names even after scope of comprehension. Is this right?
x = 'before'
a = [x for x in 1, 2, 3]
print x # this prints '3', not 'before'
