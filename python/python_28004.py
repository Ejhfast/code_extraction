# generate list from values of certain field in list of objects
objects = [{'group': 1, 'name': 'Joe'}, {'group': 2, 'name': 'Kirk'}, {'group': 1, 'name': 'Bob'}]
names = [i["name"] for i in objects]
