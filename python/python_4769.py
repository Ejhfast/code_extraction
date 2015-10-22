# Check if a predicate evaluates true for all elements in an iterable in python
allTrue = all(somePredicate(elem) for elem in someIterable)
anyTrue = any(somePredicate(elem) for elem in someIterable)
