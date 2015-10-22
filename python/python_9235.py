# How to sort dictionaries of objects by attribute value in python?
for student in (sorted(student_Dict.values(), key=operator.attrgetter('age'))):
    print(student.name)
