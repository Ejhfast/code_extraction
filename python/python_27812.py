# Iterate over non None items in Python
headers = ['Name', None, 'HW1', 'HW2', None, 'HW4', 'EX1', None, None]
for header in filter(None, headers):
    print header
