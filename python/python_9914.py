# Updating each element in collection MongoDB
for row in myColl.find():
    row['myvar'] = 123
    myColl.save(row)
