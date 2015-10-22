# Python: How to create a new list based on existing list without certain objects
a = ['house', 'bikeCT', 'car', 'bike', 'houseCT']
b = [x for x in a if 'CT' not in x]
