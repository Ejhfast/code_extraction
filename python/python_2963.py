# Finding the largest delta between two integers in a list in python
max(abs(x - y) for (x, y) in zip(values[1:], values[:-1]))
