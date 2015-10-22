# How do I add a string of numbers in python
s = raw_input()
print sum(int(c) for c in s.strip())
