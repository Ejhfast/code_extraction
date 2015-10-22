# After joining set items into a single string seperated by commas, how to assign that value to a string?
for subset in combinations(ListOfName, 3):
    arg = ','.join(subset)
    occuring(arg)
