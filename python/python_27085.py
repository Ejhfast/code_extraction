# csv unique values without considering a column
data = {}
for name, age, location, phone in csv_data:
    data[name, age] = (name, age, location, phone)
