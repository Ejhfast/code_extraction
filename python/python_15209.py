# How to sort in decreasing value first then increasing in second value
print sorted(student_tuples, key=lambda t: (-t[2], t[0]))
# [('john', 'A', 15), ('dave', 'C', 12), ('peter', 'B', 12)]
