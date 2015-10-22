# adding value limitations on list comprehension
tuple(max(0, min(tupleone[x] - tupletwo[x], 255)) for x in range(3))
