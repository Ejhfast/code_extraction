# I have a very big list of dictionaries and I want to sum the insides
d = [{'A': [3, 45, 34, 4, 2, 5, 94, 2139, 230345, 283047, 230847]}, {'B': [92374, 324, 345, 345, 45879, 34857987, 3457938457]}, {'C': [23874923874987, 2347]}]
[{x.keys()[0]:sum(x.values()[0])} for x in d]
