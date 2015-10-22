# PyMongo Look up Dictionary Value when Value is in Sub-dictionary
for person in people.find({'Father.First Name': 'Gunnar'}):
    print(person)
