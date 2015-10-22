# In Python how do I sort a list of dictionaries by a certain value of the dictionary + alphabetically?
sorted(list_of_dicts, key=lambda d: (d['Name'] == 'TOTAL', d['Name'].lower()))
